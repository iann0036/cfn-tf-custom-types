# TF::NewRelic::SyntheticsMonitor

Use this resource to create, update, and delete a synthetics monitor in New Relic.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::NewRelic::SyntheticsMonitor",
    "Properties" : {
        "<a href="#bypassheadrequest" title="BypassHeadRequest">BypassHeadRequest</a>" : <i>Boolean</i>,
        "<a href="#frequency" title="Frequency">Frequency</a>" : <i>Double</i>,
        "<a href="#locations" title="Locations">Locations</a>" : <i>[ String, ... ]</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#slathreshold" title="SlaThreshold">SlaThreshold</a>" : <i>Double</i>,
        "<a href="#status" title="Status">Status</a>" : <i>String</i>,
        "<a href="#treatredirectasfailure" title="TreatRedirectAsFailure">TreatRedirectAsFailure</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#uri" title="Uri">Uri</a>" : <i>String</i>,
        "<a href="#validationstring" title="ValidationString">ValidationString</a>" : <i>String</i>,
        "<a href="#verifyssl" title="VerifySsl">VerifySsl</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::NewRelic::SyntheticsMonitor
Properties:
    <a href="#bypassheadrequest" title="BypassHeadRequest">BypassHeadRequest</a>: <i>Boolean</i>
    <a href="#frequency" title="Frequency">Frequency</a>: <i>Double</i>
    <a href="#locations" title="Locations">Locations</a>: <i>
      - String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#slathreshold" title="SlaThreshold">SlaThreshold</a>: <i>Double</i>
    <a href="#status" title="Status">Status</a>: <i>String</i>
    <a href="#treatredirectasfailure" title="TreatRedirectAsFailure">TreatRedirectAsFailure</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#uri" title="Uri">Uri</a>: <i>String</i>
    <a href="#validationstring" title="ValidationString">ValidationString</a>: <i>String</i>
    <a href="#verifyssl" title="VerifySsl">VerifySsl</a>: <i>Boolean</i>
</pre>

## Properties

#### BypassHeadRequest

Bypass HEAD request.
* `treat_redirect_as_failure` - (Optional) Fail the monitor check if redirected.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Frequency

The interval (in minutes) at which this monitor should run.
* `status` - (Required) The monitor status (i.e. `ENABLED`, `MUTED`, `DISABLED`).
* `locations` - (Required) The locations in which this monitor should be run.
* `sla_threshold` - (Optional) The base threshold for the SLA report.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Locations

The locations in which this monitor should be run.
* `sla_threshold` - (Optional) The base threshold for the SLA report.

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The title of this monitor.
* `type` - (Required) The monitor type. Valid values are `SIMPLE`, `BROWSER`, `SCRIPT_BROWSER`, and `SCRIPT_API`.
* `frequency` - (Required) The interval (in minutes) at which this monitor should run.
* `status` - (Required) The monitor status (i.e. `ENABLED`, `MUTED`, `DISABLED`).
* `locations` - (Required) The locations in which this monitor should be run.
* `sla_threshold` - (Optional) The base threshold for the SLA report.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SlaThreshold

The base threshold for the SLA report.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Status

The monitor status (i.e. `ENABLED`, `MUTED`, `DISABLED`).
* `locations` - (Required) The locations in which this monitor should be run.
* `sla_threshold` - (Optional) The base threshold for the SLA report.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TreatRedirectAsFailure

Fail the monitor check if redirected.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The monitor type. Valid values are `SIMPLE`, `BROWSER`, `SCRIPT_BROWSER`, and `SCRIPT_API`.
* `frequency` - (Required) The interval (in minutes) at which this monitor should run.
* `status` - (Required) The monitor status (i.e. `ENABLED`, `MUTED`, `DISABLED`).
* `locations` - (Required) The locations in which this monitor should be run.
* `sla_threshold` - (Optional) The base threshold for the SLA report.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Uri

The URI for the monitor to hit.
* `validation_string` - (Optional) The string to validate against in the response.
* `verify_ssl` - (Optional) Verify SSL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ValidationString

The string to validate against in the response.
* `verify_ssl` - (Optional) Verify SSL.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### VerifySsl

Verify SSL.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

