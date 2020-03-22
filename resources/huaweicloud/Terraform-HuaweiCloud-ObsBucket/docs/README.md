# Terraform::HuaweiCloud::ObsBucket

Provides an OBS bucket resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::HuaweiCloud::ObsBucket",
    "Properties" : {
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#bucket" title="Bucket">Bucket</a>" : <i>String</i>,
        "<a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>" : <i>Boolean</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#storageclass" title="StorageClass">StorageClass</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>Boolean</i>,
        "<a href="#corsrule" title="CorsRule">CorsRule</a>" : <i>[ <a href="corsrule.md">CorsRule</a>, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ <a href="lifecyclerule.md">LifecycleRule</a>, ... ]</i>,
        "<a href="#logging" title="Logging">Logging</a>" : <i>[ <a href="logging.md">Logging</a>, ... ]</i>,
        "<a href="#website" title="Website">Website</a>" : <i>[ <a href="website.md">Website</a>, ... ]</i>,
        "<a href="#expiration" title="Expiration">Expiration</a>" : <i>[ <a href="expiration.md">Expiration</a>, ... ]</i>,
        "<a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>" : <i>[ <a href="noncurrentversionexpiration.md">NoncurrentVersionExpiration</a>, ... ]</i>,
        "<a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>" : <i>[ <a href="noncurrentversiontransition.md">NoncurrentVersionTransition</a>, ... ]</i>,
        "<a href="#transition" title="Transition">Transition</a>" : <i>[ <a href="transition.md">Transition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::HuaweiCloud::ObsBucket
Properties:
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#bucket" title="Bucket">Bucket</a>: <i>String</i>
    <a href="#forcedestroy" title="ForceDestroy">ForceDestroy</a>: <i>Boolean</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#storageclass" title="StorageClass">StorageClass</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>Boolean</i>
    <a href="#corsrule" title="CorsRule">CorsRule</a>: <i>
      - <a href="corsrule.md">CorsRule</a></i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - <a href="lifecyclerule.md">LifecycleRule</a></i>
    <a href="#logging" title="Logging">Logging</a>: <i>
      - <a href="logging.md">Logging</a></i>
    <a href="#website" title="Website">Website</a>: <i>
      - <a href="website.md">Website</a></i>
    <a href="#expiration" title="Expiration">Expiration</a>: <i>
      - <a href="expiration.md">Expiration</a></i>
    <a href="#noncurrentversionexpiration" title="NoncurrentVersionExpiration">NoncurrentVersionExpiration</a>: <i>
      - <a href="noncurrentversionexpiration.md">NoncurrentVersionExpiration</a></i>
    <a href="#noncurrentversiontransition" title="NoncurrentVersionTransition">NoncurrentVersionTransition</a>: <i>
      - <a href="noncurrentversiontransition.md">NoncurrentVersionTransition</a></i>
    <a href="#transition" title="Transition">Transition</a>: <i>
      - <a href="transition.md">Transition</a></i>
</pre>

## Properties

#### Acl

Specifies the ACL policy for a bucket. The predefined common policies are as follows: "private", "public-read", "public-read-write" and "log-delivery-write". Defaults to `private`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Bucket

Specifies the name of the bucket. Changing this parameter will create a new resource.
A bucket must be named according to the globally applied DNS naming regulations as follows:
* The name must be globally unique in OBS.
* The name must contain 3 to 63 characters. Only lowercase letters, digits, hyphens (-), and periods (.) are allowed.
* The name cannot start or end with a period (.) or hyphen (-), and cannot contain two consecutive periods (.) or contain a period (.) and a hyphen (-) adjacent to each other.
* The name cannot be an IP address.
* If the name contains any periods (.), a security certificate verification message may appear when you access the bucket or its objects by entering a domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ForceDestroy

A boolean that indicates all objects should be deleted from the bucket so that the bucket can be destroyed without error. Default to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

If specified, the region this bucket should reside in. Otherwise, the region used by the provider.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StorageClass

Specifies the storage class of the bucket. OBS provides three storage classes: "STANDARD", "WARM" (Infrequent Access) and "COLD" (Archive). Defaults to `STANDARD`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the bucket. Each tag is represented by one key-value pair.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

Whether enable versioning. Once you version-enable a bucket, it can never return to an unversioned state.
You can, however, suspend versioning on that bucket.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsRule

_Required_: No

_Type_: List of <a href="corsrule.md">CorsRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of <a href="lifecyclerule.md">LifecycleRule</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Logging

_Required_: No

_Type_: List of <a href="logging.md">Logging</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Website

_Required_: No

_Type_: List of <a href="website.md">Website</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Expiration

_Required_: No

_Type_: List of <a href="expiration.md">Expiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionExpiration

_Required_: No

_Type_: List of <a href="noncurrentversionexpiration.md">NoncurrentVersionExpiration</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NoncurrentVersionTransition

_Required_: No

_Type_: List of <a href="noncurrentversiontransition.md">NoncurrentVersionTransition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Transition

_Required_: No

_Type_: List of <a href="transition.md">Transition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### BucketDomainName

Returns the <code>BucketDomainName</code> value.

#### Id

Returns the <code>Id</code> value.

