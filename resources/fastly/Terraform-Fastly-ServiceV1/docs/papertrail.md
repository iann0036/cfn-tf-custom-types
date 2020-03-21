# Terraform::Fastly::ServiceV1 Papertrail

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#address" title="Address">Address</a>" : <i>String</i>,
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#address" title="Address">Address</a>: <i>String</i>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
</pre>

## Properties

#### Address

The address of the Papertrail endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Format

Apache-style string or VCL variables to use for log formatting. Defaults to Apache Common Log format (`%h %l %u %t %r %>s`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this Papertrail endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

Where in the generated VCL the logging call should be placed; one of: `none` or `waf_debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port associated with the address where the Papertrail endpoint can be accessed.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCondition

Name of already defined `condition` to apply. This `condition` must be of type `RESPONSE`. For detailed information about Conditionals,
see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

