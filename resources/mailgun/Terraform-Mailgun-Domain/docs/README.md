# Terraform::Mailgun::Domain

Provides a Mailgun App resource. This can be used to
create and manage applications on Mailgun.

After DNS records are set, domain verification should be triggered manually using [PUT /domains/\<domain\>/verify](https://documentation.mailgun.com/en/latest/api-domains.html#domains)

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Mailgun::Domain",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#region" title="Region">Region</a>" : <i>String</i>,
        "<a href="#spamaction" title="SpamAction">SpamAction</a>" : <i>String</i>,
        "<a href="#wildcard" title="Wildcard">Wildcard</a>" : <i>Boolean</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Mailgun::Domain
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#region" title="Region">Region</a>: <i>String</i>
    <a href="#spamaction" title="SpamAction">SpamAction</a>: <i>String</i>
    <a href="#wildcard" title="Wildcard">Wildcard</a>: <i>Boolean</i>
</pre>

## Properties

#### Name

The domain to add to Mailgun.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Region

The region where domain will be created. Default value is `us`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SpamAction

`disabled` or `tag` Disable, no spam
filtering will occur for inbound messages. Tag, messages
will be tagged with a spam header.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Wildcard

Boolean that determines whether
the domain will accept email for sub-domains.

_Required_: No

_Type_: Boolean

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

#### ReceivingRecords

Returns the <code>ReceivingRecords</code> value.

#### SendingRecords

Returns the <code>SendingRecords</code> value.

#### SmtpLogin

Returns the <code>SmtpLogin</code> value.

#### SmtpPassword

Returns the <code>SmtpPassword</code> value.

