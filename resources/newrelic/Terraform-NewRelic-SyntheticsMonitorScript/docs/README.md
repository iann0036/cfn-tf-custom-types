# Terraform::NewRelic::SyntheticsMonitorScript

CloudFormation equivalent of newrelic_synthetics_monitor_script

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::NewRelic::SyntheticsMonitorScript",
    "Properties" : {
        "<a href="#monitorid" title="MonitorId">MonitorId</a>" : <i>String</i>,
        "<a href="#text" title="Text">Text</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::NewRelic::SyntheticsMonitorScript
Properties:
    <a href="#monitorid" title="MonitorId">MonitorId</a>: <i>String</i>
    <a href="#text" title="Text">Text</a>: <i>String</i>
</pre>

## Properties

#### MonitorId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Text

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.

