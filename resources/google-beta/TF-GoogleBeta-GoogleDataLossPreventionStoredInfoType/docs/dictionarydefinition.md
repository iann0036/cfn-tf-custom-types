# TF::GoogleBeta::GoogleDataLossPreventionStoredInfoType DictionaryDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#cloudstoragepath" title="CloudStoragePath">CloudStoragePath</a>" : <i>[ <a href="cloudstoragepathdefinition.md">CloudStoragePathDefinition</a>, ... ]</i>,
    "<a href="#wordlist" title="WordList">WordList</a>" : <i>[ <a href="wordlistdefinition.md">WordListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#cloudstoragepath" title="CloudStoragePath">CloudStoragePath</a>: <i>
      - <a href="cloudstoragepathdefinition.md">CloudStoragePathDefinition</a></i>
<a href="#wordlist" title="WordList">WordList</a>: <i>
      - <a href="wordlistdefinition.md">WordListDefinition</a></i>
</pre>

## Properties

#### CloudStoragePath

_Required_: No

_Type_: List of <a href="cloudstoragepathdefinition.md">CloudStoragePathDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WordList

_Required_: No

_Type_: List of <a href="wordlistdefinition.md">WordListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

