from nixops.storage import BackendRegistration

from nixops.storage.legacy import LegacyBackend
from nixops.storage.memory import MemoryBackend
import nixops.plugins
from nixops.locks import LockDriver
from nixops.locks.noop import NoopLock
from typing import Dict, Type


class InternalPlugin(nixops.plugins.Plugin):
    def storage_backends(self) -> BackendRegistration:
        return {"legacy": LegacyBackend, "memory": MemoryBackend}

    def lock_drivers(self) -> Dict[str, Type[LockDriver]]:
        return {"noop": NoopLock}
