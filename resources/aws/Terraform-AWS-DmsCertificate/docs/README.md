# Terraform::AWS::DmsCertificate

Provides a DMS (Data Migration Service) certificate resource. DMS certificates can be created, deleted, and imported.

~> **Note:** All arguments including the PEM encoded certificate will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DmsCertificate",
    "Properties" : {
        "<a href="#certificateid" title="CertificateId">CertificateId</a>" : <i>String</i>,
        "<a href="#certificatepem" title="CertificatePem">CertificatePem</a>" : <i>String</i>,
        "<a href="#certificatewallet" title="CertificateWallet">CertificateWallet</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DmsCertificate
Properties:
    <a href="#certificateid" title="CertificateId">CertificateId</a>: <i>String</i>
    <a href="#certificatepem" title="CertificatePem">CertificatePem</a>: <i>String</i>
    <a href="#certificatewallet" title="CertificateWallet">CertificateWallet</a>: <i>String</i>
</pre>

## Properties

#### CertificateId

The certificate identifier.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificatePem

The contents of the .pem X.509 certificate file for the certificate. Either `certificate_pem` or `certificate_wallet` must be set.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CertificateWallet

The contents of the Oracle Wallet certificate for use with SSL. Either `certificate_pem` or `certificate_wallet` must be set.

_Required_: No

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

#### CertificateArn

Returns the <code>CertificateArn</code> value.

#### Id

Returns the <code>Id</code> value.

