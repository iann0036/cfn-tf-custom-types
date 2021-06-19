# TF::Linode::ObjectStorageBucket

Provides a Linode Object Storage Bucket resource. This can be used to create, modify, and delete Linodes Object Storage Buckets.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Linode::ObjectStorageBucket",
    "Properties" : {
        "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
        "<a href="#acl" title="Acl">Acl</a>" : <i>String</i>,
        "<a href="#cluster" title="Cluster">Cluster</a>" : <i>String</i>,
        "<a href="#corsenabled" title="CorsEnabled">CorsEnabled</a>" : <i>Boolean</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>,
        "<a href="#versioning" title="Versioning">Versioning</a>" : <i>Boolean</i>,
        "<a href="#cert" title="Cert">Cert</a>" : <i>[ <a href="certdefinition.md">CertDefinition</a>, ... ]</i>,
        "<a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>" : <i>[ <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Linode::ObjectStorageBucket
Properties:
    <a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
    <a href="#acl" title="Acl">Acl</a>: <i>String</i>
    <a href="#cluster" title="Cluster">Cluster</a>: <i>String</i>
    <a href="#corsenabled" title="CorsEnabled">CorsEnabled</a>: <i>Boolean</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
    <a href="#versioning" title="Versioning">Versioning</a>: <i>Boolean</i>
    <a href="#cert" title="Cert">Cert</a>: <i>
      - <a href="certdefinition.md">CertDefinition</a></i>
    <a href="#lifecyclerule" title="LifecycleRule">LifecycleRule</a>: <i>
      - <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a></i>
</pre>

## Properties

#### AccessKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Acl

The Access Control Level of the bucket using a canned ACL string. See all ACL strings [in the Linode API v4 documentation](linode.com/docs/api/object-storage/#object-storage-bucket-access-update__request-body-schema).

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cluster

The cluster of the Linode Object Storage Bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CorsEnabled

If true, the bucket will have CORS enabled for all origins.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The label of the Linode Object Storage Bucket.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Versioning

Whether to enable versioning. Once you version-enable a bucket, it can never return to an unversioned state. You can, however, suspend versioning on that bucket.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Cert

_Required_: No

_Type_: List of <a href="certdefinition.md">CertDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LifecycleRule

_Required_: No

_Type_: List of <a href="lifecycleruledefinition.md">LifecycleRuleDefinition</a>

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

