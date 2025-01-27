from django.core.management.base import BaseCommand
from main.concurrent_insertion import DatabaseInserter

class Command(BaseCommand):
    help = 'Run concurrent database insertions'

    def handle(self, *args, **kwargs):
        inserter = DatabaseInserter()
        results = inserter.run_concurrent_insertions()
        
        self.stdout.write("\nInsertion Results:\n")
        
        for model_name, model_results in results.items():
            self.stdout.write(f"\n{model_name.upper()} INSERTIONS:")
            for i, (success, error) in enumerate(model_results, 1):
                status = "SUCCESS" if success else f"FAILED: {error}"
                self.stdout.write(f"Record {i}: {status}")