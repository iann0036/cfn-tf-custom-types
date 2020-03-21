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

Names of defined backends to map the director to. Example: `[ "origin1", "origin2" ]`.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Capacity

Load balancing weight for the backends. Default `100`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Comment

An optional comment about the Director.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Unique name for this Director.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Quorum

Percentage of capacity that needs to be up for the director itself to be considered up. Default `75`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Retries

How many backends to search if it fails. Default `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Shield

Selected POP to serve as a "shield" for origin servers.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

Type of load balance group to use. Integer, 1 to 4. Values: `1` (random), `3` (hash), `4` (client).  Default `1`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

