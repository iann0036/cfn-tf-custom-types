# Terraform::OpsGenie::TeamRoutingRule Criteria Conditions

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#expectedvalue" title="ExpectedValue">ExpectedValue</a>" : <i>String</i>,
    "<a href="#field" title="Field">Field</a>" : <i>String</i>,
    "<a href="#key" title="Key">Key</a>" : <i>String</i>,
    "<a href="#not" title="Not">Not</a>" : <i>Boolean</i>,
    "<a href="#operation" title="Operation">Operation</a>" : <i>String</i>,
    "<a href="#order" title="Order">Order</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#expectedvalue" title="ExpectedValue">ExpectedValue</a>: <i>String</i>
<a href="#field" title="Field">Field</a>: <i>String</i>
<a href="#key" title="Key">Key</a>: <i>String</i>
<a href="#not" title="Not">Not</a>: <i>Boolean</i>
<a href="#operation" title="Operation">Operation</a>: <i>String</i>
<a href="#order" title="Order">Order</a>: <i>Double</i>
</pre>

## Properties

#### ExpectedValue

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Field

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Not

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operation

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

