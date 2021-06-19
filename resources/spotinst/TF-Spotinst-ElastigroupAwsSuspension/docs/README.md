# TF::Spotinst::ElastigroupAwsSuspension

Suspend AWS Elastigroup processes. This resource provide the capavility of
suspending elastigroup processes using Terraform.

For supported processes please visit: [Suspend Processes API reference](https://help.spot.io/spotinst-api/elastigroup/amazon-web-services/suspend-processes/)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Spotinst::ElastigroupAwsSuspension",
    "Properties" : {
        "<a href="#groupid" title="GroupId">GroupId</a>" : <i>String</i>,
        "<a href="#suspension" title="Suspension">Suspension</a>" : <i>[ <a href="suspensiondefinition.md">SuspensionDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Spotinst::ElastigroupAwsSuspension
Properties:
    <a href="#groupid" title="GroupId">GroupId</a>: <i>String</i>
    <a href="#suspension" title="Suspension">Suspension</a>: <i>
      - <a href="suspensiondefinition.md">SuspensionDefinition</a></i>
</pre>

## Properties

#### GroupId

Elastigroup ID to apply the suspensions on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Suspension

_Required_: No

_Type_: List of <a href="suspensiondefinition.md">SuspensionDefinition</a>

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

