# Terraform::Fastly::ServiceV1 Logentries

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#format" title="Format">Format</a>" : <i>String</i>,
    "<a href="#formatversion" title="FormatVersion">FormatVersion</a>" : <i>Double</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#placement" title="Placement">Placement</a>" : <i>String</i>,
    "<a href="#port" title="Port">Port</a>" : <i>Double</i>,
    "<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>" : <i>String</i>,
    "<a href="#token" title="Token">Token</a>" : <i>String</i>,
    "<a href="#usetls" title="UseTls">UseTls</a>" : <i>Boolean</i>
}
</pre>

### YAML

<pre>
<a href="#format" title="Format">Format</a>: <i>String</i>
<a href="#formatversion" title="FormatVersion">FormatVersion</a>: <i>Double</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#placement" title="Placement">Placement</a>: <i>String</i>
<a href="#port" title="Port">Port</a>: <i>Double</i>
<a href="#responsecondition" title="ResponseCondition">ResponseCondition</a>: <i>String</i>
<a href="#token" title="Token">Token</a>: <i>String</i>
<a href="#usetls" title="UseTls">UseTls</a>: <i>Boolean</i>
</pre>

## Properties

#### Format

Apache-style string or VCL variables to use for log formatting. Defaults to Apache Common Log format (`%h %l %u %t %r %>s`).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FormatVersion

The version of the custom logging format used for the configured endpoint. Can be either 1 (the default, version 1 log format) or 2 (the version 2 log format).

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this GCS endpoint.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Placement

Where in the generated VCL the logging call should be placed; one of: `none` or `waf_debug`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Port

The port number configured in Logentries to send logs to. Defaults to `20000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResponseCondition

Name of already defined `condition` to apply. This `condition` must be of type `RESPONSE`. For detailed information about Conditionals, see [Fastly's Documentation on Conditionals][fastly-conditionals].

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Token

Logentries Token to be used for authentication (https://logentries.com/doc/input-token/).

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UseTls

Whether to use TLS for secure logging. Defaults to `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

