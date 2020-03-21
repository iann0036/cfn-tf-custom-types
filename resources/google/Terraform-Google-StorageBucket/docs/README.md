# Terraform::Google::StorageBucket

CloudFormation equivalent of google_storage_bucket

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::StorageBucket",
    "Properties" : {
        "<a href="#bucketpolicyonly" title="BucketPolicyOnly">BucketPolicyOnly</a>" : <i>Boolean</i>,
        "<a href="#defaulteventbasedhold" title="DefaultEventBasedHold">DefaultEventBasedHold</a>" : <i>Boolean</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#labels" title="Labels">Labels</a>" : <i>[ &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;, ... ]</i>,
        "<a href="#location" title="Location">Location</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#requesterpays" title="RequesterPays">RequesterPays</a>" : <i>Boolean</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#cors" title="Cors">Cors</a>" : <i>[ &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;, ... ]</i>,
        "<a href="#encryption" title="Encryption">Encryption</a>" : <i>[ &lt;a href=&#34;encryption.md&#34;&gt;Encryption&lt;/a&gt;, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;, ... ]</i>,
        "<a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>" : <i>[ &lt;a href=&#34;retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>[ &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;, ... ]</i>,
        "<a href="#action" title="Action">Action</a>" : <i>[ &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;, ... ]</i>,
        "<a href="#condition" title="Condition">Condition</a>" : <i>[ &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::StorageBucket
Properties:
    <a href="#bucketpolicyonly" title="BucketPolicyOnly">BucketPolicyOnly</a>: <i>Boolean</i>
    <a href="#defaulteventbasedhold" title="DefaultEventBasedHold">DefaultEventBasedHold</a>: <i>Boolean</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#labels" title="Labels">Labels</a>: <i>
      - &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;</i>
    <a href="#location" title="Location">Location</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#requesterpays" title="RequesterPays">RequesterPays</a>: <i>Boolean</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#cors" title="Cors">Cors</a>: <i>
      - &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;</i>
    <a href="#encryption" title="Encryption">Encryption</a>: <i>
      - &lt;a href=&#34;encryption.md&#34;&gt;Encryption&lt;/a&gt;</i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;</i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;</i>
    <a href="#retentionpolicy" title="RetentionPolicy">RetentionPolicy</a>: <i>
      - &lt;a href=&#34;retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;</i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>
      - &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;</i>
    <a href="#website" title="Website">Website</a>: <i>
      - &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;</i>
    <a href="#action" title="Action">Action</a>: <i>
      - &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;</i>
    <a href="#condition" title="Condition">Condition</a>: <i>
      - &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;</i>
</pre>

## Properties

#### BucketPolicyOnly

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DefaultEventBasedHold

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Labels

_Required_: No

_Type_: List of &lt;a href=&#34;labels.md&#34;&gt;Labels&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Location

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RequesterPays

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cors

_Required_: No

_Type_: List of &lt;a href=&#34;cors.md&#34;&gt;Cors&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Encryption

_Required_: No

_Type_: List of &lt;a href=&#34;encryption.md&#34;&gt;Encryption&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of &lt;a href=&#34;lifecyclerule.md&#34;&gt;LifecycleRule&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of &lt;a href=&#34;logging.md&#34;&gt;Logging&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RetentionPolicy

_Required_: No

_Type_: List of &lt;a href=&#34;retentionpolicy.md&#34;&gt;RetentionPolicy&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

_Required_: No

_Type_: List of &lt;a href=&#34;versioning.md&#34;&gt;Versioning&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of &lt;a href=&#34;website.md&#34;&gt;Website&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Action

_Required_: No

_Type_: List of &lt;a href=&#34;action.md&#34;&gt;Action&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Condition

_Required_: No

_Type_: List of &lt;a href=&#34;condition.md&#34;&gt;Condition&lt;/a&gt;

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### SelfLink

Returns the &lt;code&gt;SelfLink&lt;/code&gt; value.

#### Url

Returns the &lt;code&gt;Url&lt;/code&gt; value.

