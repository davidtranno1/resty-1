class Attrs(object):
    pass


class MockDocument(object):

    def __init__(self, meta={}, content={}):

        self.type = meta.pop('type', 'T')
        self.self = meta.pop('self', 'test://mock_document')

        if 'class' in meta:
            meta['class_'] = meta.pop('class')

        self.meta = Attrs()
        self.content = Attrs()
        self.meta.__dict__.update(meta)
        self.content.__dict__.update(content)

        self._related = {}
        self._services = {}
        self._filters = {}
        self._pages = {}
        self._items = []

    def add_related(self, name, doc):
        self._related[name] = doc

    def add_service(self, name, doc):
        self._services[name] = doc

    def add_filter(self, name, doc):
        self._filters[name] = doc

    def add_item(self, doc):
        self._items.append(doc)

    def add_page(self, page_nr, doc):
        self._pages[page_nr] = doc

    def related(self, name, _):
        return self._related[name]

    def service(self, name):
        return self._services[name]

    def filter(self, name, **kwargs):
        try:
            return self._filters[name]
        except KeyError:
            raise ValueError

    def specialize(self):
        return 'specialized %s' % self.type

    def items(self):
        return self._items

    def page(self, nr):
        return self._pages[nr]


class MockStateMachine(object):

    def __init__(self):
        self._documents = {}

    def load_document(self, URI):
        return self._documents[URI]

    def add_document(self, state_id, document):
        self._documents[state_id] = document

    def specialize(self, doc):
        return 'specialized %s' % doc.type
