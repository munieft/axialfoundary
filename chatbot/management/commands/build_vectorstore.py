from __future__ import annotations

from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Build or rebuild the ChromaDB vector store from data/knowledge_base.md.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--filepath',
            type=str,
            default=None,
            help='Optional path override for the knowledge-base markdown file.',
        )

    def handle(self, *args, **options):
        # Local import keeps Django start-up fast: heavy ML deps load only when this
        # command is actually invoked.
        try:
            from chatbot.engine.embedder import build_vector_store
        except Exception as exc:
            raise CommandError(f'Could not import embedder: {exc}') from exc

        self.stdout.write('Building vector store…')
        try:
            count = build_vector_store(filepath=options.get('filepath'))
        except Exception as exc:
            raise CommandError(f'Build failed: {exc}') from exc
        self.stdout.write(self.style.SUCCESS(f'Done. {count} chunks embedded and stored.'))
