# Terraform::OpenTelekomCloud::VbsBackupShareV2

CloudFormation equivalent of opentelekomcloud_vbs_backup_share_v2

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::OpenTelekomCloud::VbsBackupShareV2",
    "Properties" : {
        "<a href="#backupid" title="BackupId">BackupId</a>" : <i>String</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#toprojectids" title="ToProjectIds">ToProjectIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#timeouts" title="Timeouts">Timeouts</a>" : <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::OpenTelekomCloud::VbsBackupShareV2
Properties:
    <a href="#backupid" title="BackupId">BackupId</a>: <i>String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#toprojectids" title="ToProjectIds">ToProjectIds</a>: <i>
      - String</i>
    <a href="#timeouts" title="Timeouts">Timeouts</a>: <i>&lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;</i>
</pre>

## Properties

#### BackupId

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ToProjectIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Timeouts

_Required_: No

_Type_: &lt;a href=&#34;timeouts.md&#34;&gt;Timeouts&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### AvailabilityZone

Returns the &lt;code&gt;AvailabilityZone&lt;/code&gt; value.

#### BackupName

Returns the &lt;code&gt;BackupName&lt;/code&gt; value.

#### BackupStatus

Returns the &lt;code&gt;BackupStatus&lt;/code&gt; value.

#### Container

Returns the &lt;code&gt;Container&lt;/code&gt; value.

#### Description

Returns the &lt;code&gt;Description&lt;/code&gt; value.

#### ServiceMetadata

Returns the &lt;code&gt;ServiceMetadata&lt;/code&gt; value.

#### ShareIds

Returns the &lt;code&gt;ShareIds&lt;/code&gt; value.

#### Size

Returns the &lt;code&gt;Size&lt;/code&gt; value.

#### SnapshotId

Returns the &lt;code&gt;SnapshotId&lt;/code&gt; value.

#### VolumeId

Returns the &lt;code&gt;VolumeId&lt;/code&gt; value.

