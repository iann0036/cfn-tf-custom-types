# Terraform::Fastly::ServiceV1 Healthcheck

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#checkinterval" title="CheckInterval">CheckInterval</a>" : <i>Double</i>,
    "<a href="#expectedresponse" title="ExpectedResponse">ExpectedResponse</a>" : <i>Double</i>,
    "<a href="#host" title="Host">Host</a>" : <i>String</i>,
    "<a href="#httpversion" title="HttpVersion">HttpVersion</a>" : <i>String</i>,
    "<a href="#initial" title="Initial">Initial</a>" : <i>Double</i>,
    "<a href="#method" title="Method">Method</a>" : <i>String</i>,
    "<a href="#name" title="Name">Name</a>" : <i>String</i>,
    "<a href="#path" title="Path">Path</a>" : <i>String</i>,
    "<a href="#threshold" title="Threshold">Threshold</a>" : <i>Double</i>,
    "<a href="#timeout" title="Timeout">Timeout</a>" : <i>Double</i>,
    "<a href="#window" title="Window">Window</a>" : <i>Double</i>
}
</pre>

### YAML

<pre>
<a href="#checkinterval" title="CheckInterval">CheckInterval</a>: <i>Double</i>
<a href="#expectedresponse" title="ExpectedResponse">ExpectedResponse</a>: <i>Double</i>
<a href="#host" title="Host">Host</a>: <i>String</i>
<a href="#httpversion" title="HttpVersion">HttpVersion</a>: <i>String</i>
<a href="#initial" title="Initial">Initial</a>: <i>Double</i>
<a href="#method" title="Method">Method</a>: <i>String</i>
<a href="#name" title="Name">Name</a>: <i>String</i>
<a href="#path" title="Path">Path</a>: <i>String</i>
<a href="#threshold" title="Threshold">Threshold</a>: <i>Double</i>
<a href="#timeout" title="Timeout">Timeout</a>: <i>Double</i>
<a href="#window" title="Window">Window</a>: <i>Double</i>
</pre>

## Properties

#### CheckInterval

How often to run the Healthcheck in milliseconds. Default `5000`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ExpectedResponse

The status code expected from the host. Default `200`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Host

The Host header to send for this Healthcheck.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HttpVersion

Whether to use version 1.0 or 1.1 HTTP. Default `1.1`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Initial

When loading a config, the initial number of probes to be seen as OK. Default `2`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Method

Which HTTP method to use. Default `HEAD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

A unique name to identify this Healthcheck.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

The path to check.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Threshold

How many Healthchecks must succeed to be considered healthy. Default `3`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeout

Timeout in milliseconds. Default `500`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Window

The number of most recent Healthcheck queries to keep for this Healthcheck. Default `5`.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

