-- Belamis : sauvegarde des révisions, une ligne par élève.
-- À coller dans Supabase > SQL Editor, puis « Run ».

create table if not exists public.progress (
  user_id    uuid primary key references auth.users (id) on delete cascade,
  data       jsonb       not null default '{}'::jsonb,
  updated_at timestamptz not null default now()
);

-- Sécurité : chaque élève ne voit et ne modifie que SA ligne.
alter table public.progress enable row level security;

drop policy if exists "progress: lire la sienne" on public.progress;
create policy "progress: lire la sienne" on public.progress
  for select to authenticated using ((select auth.uid()) = user_id);

drop policy if exists "progress: créer la sienne" on public.progress;
create policy "progress: créer la sienne" on public.progress
  for insert to authenticated with check ((select auth.uid()) = user_id);

drop policy if exists "progress: modifier la sienne" on public.progress;
create policy "progress: modifier la sienne" on public.progress
  for update to authenticated
  using ((select auth.uid()) = user_id)
  with check ((select auth.uid()) = user_id);

drop policy if exists "progress: supprimer la sienne" on public.progress;
create policy "progress: supprimer la sienne" on public.progress
  for delete to authenticated using ((select auth.uid()) = user_id);
