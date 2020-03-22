# Terraform::Alicloud::PolardbBackupPolicy

Provides a PolarDB cluster backup policy resource and used to configure cluster backup policy.

-> **NOTE:** Available in v1.66.0+. Each DB cluster has a backup policy and it will be set default values when destroying the resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::PolardbBackupPolicy",
    "Properties" : {
        "<a href="#dbclusterid" title="DbClusterId">DbClusterId</a>" : <i>String</i>,
        "<a href="#preferredbackupperiod" title="PreferredBackupPeriod">PreferredBackupPeriod</a>" : <i>[ String, ... ]</i>,
        "<a href="#preferredbackuptime" title="PreferredBackupTime">PreferredBackupTime</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::PolardbBackupPolicy
Properties:
    <a href="#dbclusterid" title="DbClusterId">DbClusterId</a>: <i>String</i>
    <a href="#preferredbackupperiod" title="PreferredBackupPeriod">PreferredBackupPeriod</a>: <i>
      - String</i>
    <a href="#preferredbackuptime" title="PreferredBackupTime">PreferredBackupTime</a>: <i>String</i>
</pre>

## Properties

#### DbClusterId

The Id of cluster that can run database.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupPeriod

PolarDB Cluster backup period. Valid values: [Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday]. Default to ["Tuesday", "Thursday", "Saturday"].

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PreferredBackupTime

PolarDB Cluster backup time, in the format of HH:mmZ- HH:mmZ. Time setting interval is one hour. Default to "02:00Z-03:00Z". China time is 8 hours behind it.

_Required_: No

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

#### BackupRetentionPeriod

Returns the <code>BackupRetentionPeriod</code> value.

#### Id

Returns the <code>Id</code> value.

