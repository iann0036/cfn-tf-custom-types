# TF::AzureRM::HdinsightHadoopCluster NetworkDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#connectiondirection" title="ConnectionDirection">ConnectionDirection</a>" : <i>String</i>,
    "<a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#connectiondirection" title="ConnectionDirection">ConnectionDirection</a>: <i>String</i>
<a href="#privatelinkenabled" title="PrivateLinkEnabled">PrivateLinkEnabled</a>: <i>Boolean</i>
</pre>

## Properties

#### ConnectionDirection

The direction of the resource provider connection. Possible values include `Inbound` or `Outbound`. Defaults to `Inbound`. Changing this forces a new resource to be created.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateLinkEnabled

Is the private link enabled? Possible values include `True` or `False`. Defaults to `False`. Changing this forces a new resource to be created.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

