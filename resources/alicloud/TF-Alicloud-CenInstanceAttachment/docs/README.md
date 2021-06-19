# TF::Alicloud::CenInstanceAttachment

Provides a CEN child instance attachment resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Alicloud::CenInstanceAttachment",
    "Properties" : {
        "<a href="#cenownerid" title="CenOwnerId">CenOwnerId</a>" : <i>Double</i>,
        "<a href="#childinstanceid" title="ChildInstanceId">ChildInstanceId</a>" : <i>String</i>,
        "<a href="#childinstanceownerid" title="ChildInstanceOwnerId">ChildInstanceOwnerId</a>" : <i>Double</i>,
        "<a href="#childinstanceregionid" title="ChildInstanceRegionId">ChildInstanceRegionId</a>" : <i>String</i>,
        "<a href="#childinstancetype" title="ChildInstanceType">ChildInstanceType</a>" : <i>String</i>,
        "<a href="#instanceid" title="InstanceId">InstanceId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Alicloud::CenInstanceAttachment
Properties:
    <a href="#cenownerid" title="CenOwnerId">CenOwnerId</a>: <i>Double</i>
    <a href="#childinstanceid" title="ChildInstanceId">ChildInstanceId</a>: <i>String</i>
    <a href="#childinstanceownerid" title="ChildInstanceOwnerId">ChildInstanceOwnerId</a>: <i>Double</i>
    <a href="#childinstanceregionid" title="ChildInstanceRegionId">ChildInstanceRegionId</a>: <i>String</i>
    <a href="#childinstancetype" title="ChildInstanceType">ChildInstanceType</a>: <i>String</i>
    <a href="#instanceid" title="InstanceId">InstanceId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### CenOwnerId

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildInstanceId

The ID of the child instance to attach.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildInstanceOwnerId

The uid of the child instance. Only used when attach a child instance of other account.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildInstanceRegionId

The region ID of the child instance to attach.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ChildInstanceType

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InstanceId

The ID of the CEN.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: <a href="timeoutsdefinition.md">TimeoutsDefinition</a>

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

#### Status

Returns the <code>Status</code> value.

