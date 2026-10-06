from memory.feedback_store import (
    load_feedbacks,
    save_feedbacks
)

from memory.embeddings import (
    get_embedding
)

from datetime import datetime


records = load_feedbacks()

for record in records:

    if "embedding" not in record:

        record["embedding"] = get_embedding(
            record["query"]
        )

    if "updated_at" not in record:

        record["updated_at"] = (
            datetime.utcnow()
            .isoformat()
        )

save_feedbacks(records)

print("Migration complete")