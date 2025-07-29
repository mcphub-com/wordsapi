import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/dpventures/api/wordsapi'

mcp = FastMCP('wordsapi')

@mcp.tool()
def is_atype_of(word: Annotated[str, Field(description='Try "hatchback".')]) -> dict: 
    '''Finds word that are more general than the given word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/hatchback/typeOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_types(word: Annotated[str, Field(description='Try "purple".')]) -> dict: 
    '''Get more specific examples of types of this word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/hasTypes'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def part_of(word: Annotated[str, Field(description='Try "finger".')]) -> dict: 
    '''The larger whole to which the word belongs.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/finger/partOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_parts(word: Annotated[str, Field(description='Try "building".')]) -> dict: 
    '''Words that are parts of the original word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/building/hasParts'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def is_an_instance_of(word: Annotated[str, Field(description='Try "einstein".')]) -> dict: 
    '''Words that the parameter word is an example of.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/einstein/instanceOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_instances(word: Annotated[str, Field(description='Try "president".')]) -> dict: 
    '''Words that are examples of the parameter word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/hasInstances'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def similar_to(word: Annotated[str, Field(description='Try "bloody".')]) -> dict: 
    '''Words that similar to the original word, but are not synonyms.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/bloody/similarTo'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def also(word: Annotated[str, Field(description='Try "bump".')]) -> dict: 
    '''Phrases of which the word is a part.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/bump/also'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def entails(word: Annotated[str, Field(description='Try "rub".')]) -> dict: 
    '''Words that are implied by the original word. Usually used for verbs.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/entails'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def member_of(word: Annotated[str, Field(description='Try "dory".')]) -> dict: 
    '''A group to which the word belongs.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/dory/memberOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_members(word: Annotated[str, Field(description='Try "cosmos".')]) -> dict: 
    '''Words that belong to the group defined by the parameter word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/cosmos/hasMembers'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def substance_of(word: Annotated[str, Field(description='')]) -> dict: 
    '''Substances to which the original word is a part of.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/substanceOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_substances(word: Annotated[str, Field(description='Try "wood".')]) -> dict: 
    '''Words that are substances of the parameter word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/wood/hasSubstances'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def in_category(word: Annotated[str, Field(description='Try "chaotic".')]) -> dict: 
    '''The domain category to which the original word belongs.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/chaotic/inCategory'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_categories(word: Annotated[str, Field(description='Try "math".')]) -> dict: 
    '''Categories of the parameter word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/hasCategories'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def usage_of(word: Annotated[str, Field(description='Try "advil".')]) -> dict: 
    '''Words that the original word is a domain usage of.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/advil/usageOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def has_usages(word: Annotated[str, Field(description='Try "colloquialism".')]) -> dict: 
    '''Words that are examples of the domain the original word defines.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/colloquialism/hasUsages'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def in_region(word: Annotated[str, Field(description='Try "chips".')]) -> dict: 
    '''Geographical areas where the word is used.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/chips/inRegion'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def region_of(word: Annotated[str, Field(description='Try "canada".')]) -> dict: 
    '''Words used in the specified geographical area.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/canada/regionOf'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pertains_to(words: Annotated[str, Field(description='Try ".22-caliber".')]) -> dict: 
    '''Words to which the original word is relevant.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/.22-caliber/pertainsTo'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'words': words,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def synonyms(word: Annotated[str, Field(description='Try "lovely".')]) -> dict: 
    '''Get synonyms of a word'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/lovely/synonyms'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def word(word: Annotated[str, Field(description='Try "example".')]) -> dict: 
    '''Retrieve information about a word. Results can include definitions, part of speech, synonyms, related words, syllables, and pronunciation. This method is useful to see which relationships are attached to which definition and part of speech of a word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def definitions(word: Annotated[str, Field(description='Try "incredible".')]) -> dict: 
    '''Get definitions of a word, including the part of speech.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/incredible/definitions'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def examples(word: Annotated[str, Field(description='Try "uneventful".')]) -> dict: 
    '''Get examples of how the word is used.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/examples'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def rhymes(word: Annotated[str, Field(description='')]) -> dict: 
    '''Get a list of words that rhyme with the given word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/rhymes'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def antonyms(word: Annotated[str, Field(description='Try "free".')]) -> dict: 
    '''Get antonyms (opposites) of a word.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/%7Bword%7D/antonyms'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def pronunciation(word: Annotated[str, Field(description='Try "wind". It sounds different depending on if its a noun or a verb.')]) -> dict: 
    '''How to pronounce a word, according to the International Phonetic Alphabet. May include multiple results if the word is pronounced differently depending on its part of speech.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/wind/pronunciation'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def syllables(word: Annotated[str, Field(description='Try "incredible".')]) -> dict: 
    '''Returns the word broken down into syllables.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/incredible/syllables'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def frequency(word: Annotated[str, Field(description='Try "apartment"')]) -> dict: 
    '''Expands upon the frequeny score returned by the main /words/{word} endpoint. Returns zipf, a score indicating how common the word is in the English language, with a range of 1 to 7; perMillion, the number of times the word is likely to appear in a corpus of one million English words; and diversity, a 0-1 scale the shows the likelyhood of the word appearing in an English document that is part of a corpus.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/apartment/frequency'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'word': word,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def random() -> dict: 
    '''Retrieve a random word, optionally matching a search criteria. You can use the same search criteria as the "Search" endpoint.'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(letterPattern: Annotated[Union[str, None], Field(description='Find words whose letters match the regular expression.')] = None,
           pronunciationpattern: Annotated[Union[str, None], Field(description='Find words whose pronunciation matches the regular expression.')] = None,
           partofspeech: Annotated[Union[str, None], Field(description='The matching word must have at least one definition with this part of speech.')] = None,
           lettersmin: Annotated[Union[str, None], Field(description='The minimum number of letters the word must have.')] = None,
           letters: Annotated[Union[str, None], Field(description='The number of letters the word must have.')] = None,
           lettersMax: Annotated[Union[str, None], Field(description='The maximum number of letters the word can have.')] = None,
           soundsmax: Annotated[Union[str, None], Field(description='The maximum number of phonemes (sounds) the word can have.')] = None,
           sounds: Annotated[Union[str, None], Field(description='The number of phonemes (sounds) the word mush have.')] = None,
           soundsMin: Annotated[Union[str, None], Field(description='The minimum number of phonemes (sounds) the word can have.')] = None,
           syllables: Annotated[Union[str, None], Field(description='The number of syllables the word must have.')] = None,
           syllablesMin: Annotated[Union[str, None], Field(description='The minimum number of syllables the word can have.')] = None,
           syllablesMax: Annotated[Union[str, None], Field(description='The maximum number of syllables the word can have.')] = None,
           limit: Annotated[Union[str, None], Field(description='The number of results to return per page. Must be between 1 and 100. Default is 100.')] = None,
           page: Annotated[Union[str, None], Field(description='The page of results to return. The default is page 1.')] = None,
           frequencymin: Annotated[Union[str, None], Field(description='The minimum frequency score of words to return. You can use this to limit your search to words that people are familiar with (like "go", with a frequency of 6.98). The range is from 1.74 - 8.03.')] = None,
           frequencymax: Annotated[Union[str, None], Field(description='The maximum frequency score of words to return. You can use this to limit your search to words that aren\'t seen as frequently (like "zygote", with a frequency of 2.55). The range is from 1.74 - 8.03.')] = None,
           hasDetails: Annotated[Union[str, None], Field(description='A comma delimited list of detail types the word has. For instance, to find words that have both "typeOf" and "hasCategories" relationship, you would send "hasDetails=typeOf,hasCategories".')] = None) -> dict: 
    '''Search for words matching the parameters you provide. For more examples, please see the documentation on the website. https://www.wordsapi.com/docs#search'''
    url = 'https://wordsapiv1.p.rapidapi.com/words/'
    headers = {'x-rapidapi-host': 'wordsapiv1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'letterPattern': letterPattern,
        'pronunciationpattern': pronunciationpattern,
        'partofspeech': partofspeech,
        'lettersmin': lettersmin,
        'letters': letters,
        'lettersMax': lettersMax,
        'soundsmax': soundsmax,
        'sounds': sounds,
        'soundsMin': soundsMin,
        'syllables': syllables,
        'syllablesMin': syllablesMin,
        'syllablesMax': syllablesMax,
        'limit': limit,
        'page': page,
        'frequencymin': frequencymin,
        'frequencymax': frequencymax,
        'hasDetails': hasDetails,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
