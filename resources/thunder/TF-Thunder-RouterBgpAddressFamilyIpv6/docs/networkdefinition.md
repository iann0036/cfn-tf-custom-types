# TF::Thunder::RouterBgpAddressFamilyIpv6 NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#ipv6networklist" title="Ipv6NetworkList">Ipv6NetworkList</a>" : <i>[ <a href="ipv6networklistdefinition.md">Ipv6NetworkListDefinition</a>, ... ]</i>,
    "<a href="#synchronization" title="Synchronization">Synchronization</a>" : <i>[ <a href="synchronizationdefinition.md">SynchronizationDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#ipv6networklist" title="Ipv6NetworkList">Ipv6NetworkList</a>: <i>
      - <a href="ipv6networklistdefinition.md">Ipv6NetworkListDefinition</a></i>
<a href="#synchronization" title="Synchronization">Synchronization</a>: <i>
      - <a href="synchronizationdefinition.md">SynchronizationDefinition</a></i>
</pre>

## Properties

#### Ipv6NetworkList

_Required_: No

_Type_: List of <a href="ipv6networklistdefinition.md">Ipv6NetworkListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Synchronization

_Required_: No

_Type_: List of <a href="synchronizationdefinition.md">SynchronizationDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

