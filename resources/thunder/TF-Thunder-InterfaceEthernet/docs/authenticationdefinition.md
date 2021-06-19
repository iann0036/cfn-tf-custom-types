# TF::Thunder::InterfaceEthernet AuthenticationDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#keychainlist" title="KeyChainList">KeyChainList</a>" : <i>[ <a href="keychainlistdefinition.md">KeyChainListDefinition</a>, ... ]</i>,
    "<a href="#modelist" title="ModeList">ModeList</a>" : <i>[ <a href="modelistdefinition.md">ModeListDefinition</a>, ... ]</i>,
    "<a href="#sendonlylist" title="SendOnlyList">SendOnlyList</a>" : <i>[ <a href="sendonlylistdefinition.md">SendOnlyListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#keychainlist" title="KeyChainList">KeyChainList</a>: <i>
      - <a href="keychainlistdefinition.md">KeyChainListDefinition</a></i>
<a href="#modelist" title="ModeList">ModeList</a>: <i>
      - <a href="modelistdefinition.md">ModeListDefinition</a></i>
<a href="#sendonlylist" title="SendOnlyList">SendOnlyList</a>: <i>
      - <a href="sendonlylistdefinition.md">SendOnlyListDefinition</a></i>
</pre>

## Properties

#### KeyChainList

_Required_: No

_Type_: List of <a href="keychainlistdefinition.md">KeyChainListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ModeList

_Required_: No

_Type_: List of <a href="modelistdefinition.md">ModeListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendOnlyList

_Required_: No

_Type_: List of <a href="sendonlylistdefinition.md">SendOnlyListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

