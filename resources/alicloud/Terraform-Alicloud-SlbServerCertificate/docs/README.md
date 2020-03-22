# Terraform::Alicloud::SlbServerCertificate

A Load Balancer Server Certificate is an ssl Certificate used by the listener of the protocol https.

For information about slb and how to use it, see [What is Server Load Balancer](https://www.alibabacloud.com/help/doc-detail/27539.htm).

For information about Server Certificate and how to use it, see [Configure Server Certificate](https://www.alibabacloud.com/help/doc-detail/85968.htm).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SlbServerCertificate",
    "Properties" : {
        "<a href="#alicloudcertifacteid" title="AlicloudCertifacteId">AlicloudCertifacteId</a>" : <i>String</i>,
        "<a href="#alicloudcertifactename" title="AlicloudCertifacteName">AlicloudCertifacteName</a>" : <i>String</i>,
        "<a href="#alicloudcertificateid" title="AlicloudCertificateId">AlicloudCertificateId</a>" : <i>String</i>,
        "<a href="#alicloudcertificatename" title="AlicloudCertificateName">AlicloudCertificateName</a>" : <i>String</i>,
        "<a href="#alicloudcertificateregionid" title="AlicloudCertificateRegionId">AlicloudCertificateRegionId</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#privatekey" title="PrivateKey">PrivateKey</a>" : <i>String</i>,
        "<a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>" : <i>String</i>,
        "<a href="#servercertificate" title="ServerCertificate">ServerCertificate</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ <a href="tags.md">Tags</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SlbServerCertificate
Properties:
    <a href="#alicloudcertifacteid" title="AlicloudCertifacteId">AlicloudCertifacteId</a>: <i>String</i>
    <a href="#alicloudcertifactename" title="AlicloudCertifacteName">AlicloudCertifacteName</a>: <i>String</i>
    <a href="#alicloudcertificateid" title="AlicloudCertificateId">AlicloudCertificateId</a>: <i>String</i>
    <a href="#alicloudcertificatename" title="AlicloudCertificateName">AlicloudCertificateName</a>: <i>String</i>
    <a href="#alicloudcertificateregionid" title="AlicloudCertificateRegionId">AlicloudCertificateRegionId</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#privatekey" title="PrivateKey">PrivateKey</a>: <i>String</i>
    <a href="#resourcegroupid" title="ResourceGroupId">ResourceGroupId</a>: <i>String</i>
    <a href="#servercertificate" title="ServerCertificate">ServerCertificate</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - <a href="tags.md">Tags</a></i>
</pre>

## Properties

#### AlicloudCertifacteId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudCertifacteName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudCertificateId

an id of server certificate ssued/proxied by alibaba cloud. but it is not supported on the international site of alibaba cloud now.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudCertificateName

the name of the certificate specified by `alicloud_certificate_id`.but it is not supported on the international site of alibaba cloud now.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AlicloudCertificateRegionId

the region of the certificate specified by `alicloud_certificate_id`. but it is not supported on the international site of alibaba cloud now.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

Name of the Server Certificate.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PrivateKey

the content of privat key of the ssl certificate specified by `server_certificate`. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResourceGroupId

The Id of resource group which the slb server certificate belongs.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificate

the content of the ssl certificate. where `alicloud_certificate_id` is null, it is required, otherwise it is ignored.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A mapping of tags to assign to the resource.

_Required_: No

_Type_: List of <a href="tags.md">Tags</a>

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

