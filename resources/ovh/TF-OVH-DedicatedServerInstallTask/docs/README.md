# TF::OVH::DedicatedServerInstallTask

Install your Dedicated Server.

> NOTE: After some delay, if the task is marked as `done`, the Provider
may purge it. To avoid raising errors when terraform refreshes its plan, 
404 errors are ignored on Resource Read, thus some information may be lost
after a while.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::OVH::DedicatedServerInstallTask",
    "Properties" : {
        "<a href="#bootidondestroy" title="BootidOnDestroy">BootidOnDestroy</a>" : <i>Double</i>,
        "<a href="#partitionschemename" title="PartitionSchemeName">PartitionSchemeName</a>" : <i>String</i>,
        "<a href="#servicename" title="ServiceName">ServiceName</a>" : <i>String</i>,
        "<a href="#templatename" title="TemplateName">TemplateName</a>" : <i>String</i>,
        "<a href="#details" title="Details">Details</a>" : <i>[ <a href="detailsdefinition.md">DetailsDefinition</a>, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::OVH::DedicatedServerInstallTask
Properties:
    <a href="#bootidondestroy" title="BootidOnDestroy">BootidOnDestroy</a>: <i>Double</i>
    <a href="#partitionschemename" title="PartitionSchemeName">PartitionSchemeName</a>: <i>String</i>
    <a href="#servicename" title="ServiceName">ServiceName</a>: <i>String</i>
    <a href="#templatename" title="TemplateName">TemplateName</a>: <i>String</i>
    <a href="#details" title="Details">Details</a>: <i>
      - <a href="detailsdefinition.md">DetailsDefinition</a></i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### BootidOnDestroy

If set, reboot the server on the specified boot id during destroy phase.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PartitionSchemeName

Partition scheme name.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceName

The service_name of your dedicated server.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TemplateName

Template name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Details

_Required_: No

_Type_: List of <a href="detailsdefinition.md">DetailsDefinition</a>

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

#### Comment

Returns the <code>Comment</code> value.

#### DoneDate

Returns the <code>DoneDate</code> value.

#### Function

Returns the <code>Function</code> value.

#### Id

Returns the <code>Id</code> value.

#### LastUpdate

Returns the <code>LastUpdate</code> value.

#### StartDate

Returns the <code>StartDate</code> value.

#### Status

Returns the <code>Status</code> value.

