# TF::AWS::SesDomainMailFrom

Provides an SES domain MAIL FROM resource.

~> **NOTE:** For the MAIL FROM domain to be fully usable, this resource should be paired with the [aws_ses_domain_identity resource](/docs/providers/aws/r/ses_domain_identity.html). To validate the MAIL FROM domain, a DNS MX record is required. To pass SPF checks, a DNS TXT record may also be required. See the [Amazon SES MAIL FROM documentation](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/mail-from-set.html) for more information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SesDomainMailFrom",
    "Properties" : {
        "<a href="#behavioronmxfailure" title="BehaviorOnMxFailure">BehaviorOnMxFailure</a>" : <i>String</i>,
        "<a href="#domain" title="Domain">Domain</a>" : <i>String</i>,
        "<a href="#mailfromdomain" title="MailFromDomain">MailFromDomain</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SesDomainMailFrom
Properties:
    <a href="#behavioronmxfailure" title="BehaviorOnMxFailure">BehaviorOnMxFailure</a>: <i>String</i>
    <a href="#domain" title="Domain">Domain</a>: <i>String</i>
    <a href="#mailfromdomain" title="MailFromDomain">MailFromDomain</a>: <i>String</i>
</pre>

## Properties

#### BehaviorOnMxFailure

The action that you want Amazon SES to take if it cannot successfully read the required MX record when you send an email. Defaults to `UseDefaultValue`. See the [SES API documentation](https://docs.aws.amazon.com/ses/latest/APIReference/API_SetIdentityMailFromDomain.html) for more information.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Domain

Verified domain name to generate DKIM tokens for.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MailFromDomain

Subdomain (of above domain) which is to be used as MAIL FROM address (Required for DMARC validation).

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

#### Id

Returns the <code>Id</code> value.

