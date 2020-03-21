# Terraform::Alicloud::SlbDomainExtension

HTTPS listeners of guaranteed-performance SLB support configuring multiple certificates, allowing you to forward requests with different domain names to different backend servers.
Please refer to the [documentation](https://www.alibabacloud.com/help/doc-detail/85956.htm?spm=a2c63.p38356.b99.40.1c881563Co8p6w) for details.

-> **NOTE:** Available in 1.60.0+

-> **NOTE:** The instance with shared loadBalancerSpec doesn't support domainExtension.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Alicloud::SlbDomainExtension",
    "Properties" : {
        "<a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>" : <i>Boolean</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#frontendport" title="FrontendPort">FrontendPort</a>" : <i>Double</i>,
        "<a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>" : <i>String</i>,
        "<a href="#servercertificateid" title="ServerCertificateId">ServerCertificateId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Alicloud::SlbDomainExtension
Properties:
    <a href="#deleteprotectionvalidation" title="DeleteProtectionValidation">DeleteProtectionValidation</a>: <i>Boolean</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#frontendport" title="FrontendPort">FrontendPort</a>: <i>Double</i>
    <a href="#loadbalancerid" title="LoadBalancerId">LoadBalancerId</a>: <i>String</i>
    <a href="#servercertificateid" title="ServerCertificateId">ServerCertificateId</a>: <i>String</i>
</pre>

## Properties

#### DeleteProtectionValidation

Checking DeleteProtection of SLB instance before deleting. If true, this resource will not be deleted when its SLB instance enabled DeleteProtection. Default to false.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

The domain name,.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FrontendPort

The frontend port used by the HTTPS listener of the SLB instance. Valid values: 1–65535.

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LoadBalancerId

The ID of the SLB instance.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServerCertificateId

The ID of the certificate used by the domain name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

