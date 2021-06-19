# TF::IONOSCloud::Group

Manages groups and group privileges on IonosCloud.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::IONOSCloud::Group",
    "Properties" : {
        "<a href="#accessactivitylog" title="AccessActivityLog">AccessActivityLog</a>" : <i>Boolean</i>,
        "<a href="#createbackupunit" title="CreateBackupUnit">CreateBackupUnit</a>" : <i>Boolean</i>,
        "<a href="#createdatacenter" title="CreateDatacenter">CreateDatacenter</a>" : <i>Boolean</i>,
        "<a href="#createinternetaccess" title="CreateInternetAccess">CreateInternetAccess</a>" : <i>Boolean</i>,
        "<a href="#createk8scluster" title="CreateK8sCluster">CreateK8sCluster</a>" : <i>Boolean</i>,
        "<a href="#createpcc" title="CreatePcc">CreatePcc</a>" : <i>Boolean</i>,
        "<a href="#createsnapshot" title="CreateSnapshot">CreateSnapshot</a>" : <i>Boolean</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#reserveip" title="ReserveIp">ReserveIp</a>" : <i>Boolean</i>,
        "<a href="#s3privilege" title="S3Privilege">S3Privilege</a>" : <i>Boolean</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
    }
}
</pre>

### YAML

<pre>
Type: TF::IONOSCloud::Group
Properties:
    <a href="#accessactivitylog" title="AccessActivityLog">AccessActivityLog</a>: <i>Boolean</i>
    <a href="#createbackupunit" title="CreateBackupUnit">CreateBackupUnit</a>: <i>Boolean</i>
    <a href="#createdatacenter" title="CreateDatacenter">CreateDatacenter</a>: <i>Boolean</i>
    <a href="#createinternetaccess" title="CreateInternetAccess">CreateInternetAccess</a>: <i>Boolean</i>
    <a href="#createk8scluster" title="CreateK8sCluster">CreateK8sCluster</a>: <i>Boolean</i>
    <a href="#createpcc" title="CreatePcc">CreatePcc</a>: <i>Boolean</i>
    <a href="#createsnapshot" title="CreateSnapshot">CreateSnapshot</a>: <i>Boolean</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#reserveip" title="ReserveIp">ReserveIp</a>: <i>Boolean</i>
    <a href="#s3privilege" title="S3Privilege">S3Privilege</a>: <i>Boolean</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i><a href="timeoutsdefinition.md">TimeoutsDefinition</a></i>
</pre>

## Properties

#### AccessActivityLog

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateBackupUnit

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateDatacenter

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateInternetAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateK8sCluster

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreatePcc

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CreateSnapshot

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ReserveIp

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### S3Privilege

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

_Required_: No

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

#### Users

Returns the <code>Users</code> value.

