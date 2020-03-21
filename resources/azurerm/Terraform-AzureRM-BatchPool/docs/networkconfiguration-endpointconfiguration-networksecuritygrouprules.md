# Terraform::AzureRM::BatchPool NetworkConfiguration EndpointConfiguration NetworkSecurityGroupRules

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#access" title="Access">Access</a>" : <i>String</i>,
    "<a href="#priority" title="Priority">Priority</a>" : <i>Double</i>,
    "<a href="#sourceaddressprefix" title="SourceAddressPrefix">SourceAddressPrefix</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#access" title="Access">Access</a>: <i>String</i>
<a href="#priority" title="Priority">Priority</a>: <i>Double</i>
<a href="#sourceaddressprefix" title="SourceAddressPrefix">SourceAddressPrefix</a>: <i>String</i>
</pre>

## Properties

#### Access

The action that should be taken for a specified IP address, subnet range or tag. Acceptable values are `Allow` and `Deny`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Priority

The priority for this rule. The value must be at least `150`. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SourceAddressPrefix

The source address prefix or tag to match for the rule. Changing this forces a new resource to be created.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

