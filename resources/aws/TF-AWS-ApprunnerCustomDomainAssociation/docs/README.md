# TF::AWS::ApprunnerCustomDomainAssociation

Manages an App Runner Custom Domain association.

~> **NOTE:** After creation, you must use the information in the `certification_validation_records` attribute to add CNAME records to your Domain Name System (DNS). For each mapped domain name, add a mapping to the target App Runner subdomain (found in the `dns_target` attribute) and one or more certificate validation records. App Runner then performs DNS validation to verify that you own or control the domain name you associated. App Runner tracks domain validity in a certificate stored in AWS Certificate Manager (ACM).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::ApprunnerCustomDomainAssociation",
    "Properties" : {
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#enablewwwsubdomain" title="EnableWwwSubdomain">EnableWwwSubdomain</a>" : <i>Boolean</i>,
        "<a href="#servicearn" title="ServiceArn">ServiceArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::ApprunnerCustomDomainAssociation
Properties:
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#enablewwwsubdomain" title="EnableWwwSubdomain">EnableWwwSubdomain</a>: <i>Boolean</i>
    <a href="#servicearn" title="ServiceArn">ServiceArn</a>: <i>String</i>
</pre>

## Properties

#### DomainName

The custom domain endpoint to association. Specify a base domain e.g. `example.com` or a subdomain e.g. `subdomain.example.com`.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EnableWwwSubdomain

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ServiceArn

The ARN of the App Runner service.

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

#### CertificateValidationRecords

Returns the <code>CertificateValidationRecords</code> value.

#### DnsTarget

Returns the <code>DnsTarget</code> value.

#### Id

Returns the <code>Id</code> value.

#### Status

Returns the <code>Status</code> value.

