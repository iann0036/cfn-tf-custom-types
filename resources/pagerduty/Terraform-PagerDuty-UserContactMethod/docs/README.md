# Terraform::PagerDuty::UserContactMethod

A [contact method](https://v2.developer.pagerduty.com/v2/page/api-reference#!/Users/get_users_id_contact_methods) is a contact method for a PagerDuty user (email, phone or SMS).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::PagerDuty::UserContactMethod",
    "Properties" : {
        "<a href="#address" title="Address">Address</a>" : <i>String</i>,
        "<a href="#countrycode" title="CountryCode">CountryCode</a>" : <i>Double</i>,
        "<a href="#label" title="Label">Label</a>" : <i>String</i>,
        "<a href="#sendshortemail" title="SendShortEmail">SendShortEmail</a>" : <i>Boolean</i>,
        "<a href="#type" title="Type">Type</a>" : <i>String</i>,
        "<a href="#userid" title="UserId">UserId</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::PagerDuty::UserContactMethod
Properties:
    <a href="#address" title="Address">Address</a>: <i>String</i>
    <a href="#countrycode" title="CountryCode">CountryCode</a>: <i>Double</i>
    <a href="#label" title="Label">Label</a>: <i>String</i>
    <a href="#sendshortemail" title="SendShortEmail">SendShortEmail</a>: <i>Boolean</i>
    <a href="#type" title="Type">Type</a>: <i>String</i>
    <a href="#userid" title="UserId">UserId</a>: <i>String</i>
</pre>

## Properties

#### Address

The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CountryCode

The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Label

The label (e.g., "Work", "Mobile", etc.).
* `address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SendShortEmail

Send an abbreviated email message instead of the standard email output.
* `country_code` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Type

The contact method type. May be (`email_contact_method`, `phone_contact_method`, `sms_contact_method`, `push_notification_contact_method`).
* `send_short_email` - (Optional) Send an abbreviated email message instead of the standard email output.
* `country_code` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserId

The ID of the user.
* `type` - (Required) The contact method type. May be (`email_contact_method`, `phone_contact_method`, `sms_contact_method`, `push_notification_contact_method`).
* `send_short_email` - (Optional) Send an abbreviated email message instead of the standard email output.
* `country_code` - (Optional) The 1-to-3 digit country calling code. Required when using `phone_contact_method` or `sms_contact_method`.
* `label` - (Required) The label (e.g., "Work", "Mobile", etc.).
* `address` - (Required) The "address" to deliver to: `email`, `phone number`, etc., depending on the type.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the Id.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Blacklisted

Returns the <code>Blacklisted</code> value.

#### Enabled

Returns the <code>Enabled</code> value.

#### Id

Returns the <code>Id</code> value.

