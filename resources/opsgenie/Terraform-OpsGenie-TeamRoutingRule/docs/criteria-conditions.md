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

(Required) Specifies which alert field will be used in condition. Possible values are message, alias, description, source, entity, tags, actions, extra-properties, recipients, teams or priority.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Key

(Optional) If field is set as extra-properties, key could be used for key-value pair.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Not

(Optional) Indicates behaviour of the given operation. Default value is false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Operation

(true) It is the operation that will be executed for the given field and key. Possible operations are matches, contains, starts-with, ends-with, equals, contains-key, contains-value, greater-than, less-than, is-empty and equals-ignore-whitespace.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Order

(Optional) Order of the condition in conditions list.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

