# TF::AWS::AmplifyDomainAssociation

Provides an Amplify Domain Association resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::AmplifyDomainAssociation",
    "Properties" : {
        "<a href="#appid" title="AppId">AppId</a>" : <i>String</i>,
        "<a href="#domainname" title="DomainName">DomainName</a>" : <i>String</i>,
        "<a href="#waitforverification" title="WaitForVerification">WaitForVerification</a>" : <i>Boolean</i>,
        "<a href="#subdomain" title="SubDomain">SubDomain</a>" : <i>[ <a href="subdomaindefinition.md">SubDomainDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::AmplifyDomainAssociation
Properties:
    <a href="#appid" title="AppId">AppId</a>: <i>String</i>
    <a href="#domainname" title="DomainName">DomainName</a>: <i>String</i>
    <a href="#waitforverification" title="WaitForVerification">WaitForVerification</a>: <i>Boolean</i>
    <a href="#subdomain" title="SubDomain">SubDomain</a>: <i>
      - <a href="subdomaindefinition.md">SubDomainDefinition</a></i>
</pre>

## Properties

#### AppId

The unique ID for an Amplify app.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DomainName

The domain name for the domain association.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### WaitForVerification

If enabled, the resource will wait for the domain association status to change to `PENDING_DEPLOYMENT` or `AVAILABLE`. Setting this to `false` will skip the process. Default: `true`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubDomain

_Required_: No

_Type_: List of <a href="subdomaindefinition.md">SubDomainDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### CertificateVerificationDnsRecord

Returns the <code>CertificateVerificationDnsRecord</code> value.

#### Id

Returns the <code>Id</code> value.
