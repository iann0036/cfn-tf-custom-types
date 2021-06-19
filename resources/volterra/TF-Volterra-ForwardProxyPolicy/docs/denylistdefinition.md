# TF::Volterra::ForwardProxyPolicy DenyListDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#defaultactionallow" title="DefaultActionAllow">DefaultActionAllow</a>" : <i>Boolean</i>,
    "<a href="#defaultactiondeny" title="DefaultActionDeny">DefaultActionDeny</a>" : <i>Boolean</i>,
    "<a href="#defaultactionnextpolicy" title="DefaultActionNextPolicy">DefaultActionNextPolicy</a>" : <i>Boolean</i>,
    "<a href="#destlist" title="DestList">DestList</a>" : <i>[ <a href="destlistdefinition.md">DestListDefinition</a>, ... ]</i>,
    "<a href="#httplist" title="HttpList">HttpList</a>" : <i>[ <a href="httplistdefinition.md">HttpListDefinition</a>, ... ]</i>,
    "<a href="#tlslist" title="TlsList">TlsList</a>" : <i>[ <a href="tlslistdefinition.md">TlsListDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#defaultactionallow" title="DefaultActionAllow">DefaultActionAllow</a>: <i>Boolean</i>
<a href="#defaultactiondeny" title="DefaultActionDeny">DefaultActionDeny</a>: <i>Boolean</i>
<a href="#defaultactionnextpolicy" title="DefaultActionNextPolicy">DefaultActionNextPolicy</a>: <i>Boolean</i>
<a href="#destlist" title="DestList">DestList</a>: <i>
      - <a href="destlistdefinition.md">DestListDefinition</a></i>
<a href="#httplist" title="HttpList">HttpList</a>: <i>
      - <a href="httplistdefinition.md">HttpListDefinition</a></i>
<a href="#tlslist" title="TlsList">TlsList</a>: <i>
      - <a href="tlslistdefinition.md">TlsListDefinition</a></i>
</pre>

## Properties

#### DefaultActionAllow

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultActionDeny

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultActionNextPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DestList

_Required_: No

_Type_: List of <a href="destlistdefinition.md">DestListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpList

_Required_: No

_Type_: List of <a href="httplistdefinition.md">HttpListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TlsList

_Required_: No

_Type_: List of <a href="tlslistdefinition.md">TlsListDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

