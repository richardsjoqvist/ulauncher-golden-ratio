import logging
from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction

logger = logging.getLogger(__name__)

class GoldenRatioExtension(Extension):

    def __init__(self):
        logger.info('init GoldenRatio Extension')
        super(GoldenRatioExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):

        gr = int(event.get_argument())

        if gr > 0:
            gr = (gr * 1.618) - gr
            items = []
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='Golden ratio: %s' % gr,
                                             description='Press \'enter\' to copy to clipboard.',
                                             on_enter=CopyToClipboardAction(str(gr))
                                            ))

        return RenderResultListAction(items)

if __name__ == '__main__':
    GoldenRatioExtension().run()
