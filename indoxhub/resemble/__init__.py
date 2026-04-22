"""Resemble AI namespace for the IndoxHub client.

Usage:
    client = Client(api_key="...")
    voices = client.resemble.tts.list_voices()
    audio = client.resemble.tts.synthesize(voice_uuid="...", text="Hello")
"""

from .agents import _Agents, _AgentTools, _AgentWebhooks, _KnowledgeBase
from .audio_jobs import _AudioJobs
from .identity import _Identity
from .projects import _Projects
from .recordings import _Recordings
from .safety import _Safety
from .stt import _STT
from .tts import _TTS
from .uploads import _Uploads
from .voice_design import _VoiceDesign
from .voices import _Voices
from .watermark import _Watermark

__all__ = ["ResembleAPI"]


class ResembleAPI:
    """Namespace exposing the server's /api/v1/resemble/* surface."""

    def __init__(self, client):
        self._client = client
        self.tts = _TTS(client)
        self.voices = _Voices(client)
        self.recordings = _Recordings(client)
        self.voice_design = _VoiceDesign(client)
        self.stt = _STT(client)
        self.audio_jobs = _AudioJobs(client)
        self.safety = _Safety(client)
        self.watermark = _Watermark(client)
        self.identity = _Identity(client)
        self.projects = _Projects(client)
        self.uploads = _Uploads(client)
        self.agents = _Agents(client)
        self.agent_tools = _AgentTools(client)
        self.agent_webhooks = _AgentWebhooks(client)
        self.knowledge_base = _KnowledgeBase(client)
