# Terraform::Fastly::ServiceV1 Director

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#backends" title="Backends">Backends</a>" : <i>[ String, ... ]</i>,
    "<a href="#capacity" title="Capacity">Capacity</a>" : <i>Double</i>,
    "<a href="#comment" title="Comment">Comment</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#quorum" title="Quorum">Quorum</a>" : <i>Double</i>,
    "<a href="#retries" title="Retries">Retries</a>" : <i>Double</i>,
    "<a href="#shield" title="Shield">Shield</a>" : <i>String</i>,
    "<a href="#type" title="Type">Type</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#backends" title="Backends">Backends</a>: <i>
      - String</i>
<a href="#capacity" title="Capacity">Capacity</a>: <i>Double</i>
<a href="#comment" title="Comment">Comment</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#quorum" title="Quorum">Quorum</a>: <i>Double</i>
<a href="#retries" title="Retries">Retries</a>: <i>Double</i>
<a href="#shield" title="Shield">Shield</a>: <i>String</i>
<a href="#type" title="Type">Type</a>: <i>Double</i>
</pre>

## Properties

#### Backends

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quorum

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shield

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

