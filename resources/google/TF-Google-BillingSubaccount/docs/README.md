# TF::Google::BillingSubaccount

Allows creation and management of a Google Cloud Billing Subaccount.

!> **WARNING:** Deleting this Terraform resource will not delete or close the billing subaccount.

```hcl
resource "google_billing_subaccount" "subaccount" {
    display_name = "My Billing Account"
    master_billing_account = "012345-567890-ABCDEF"
}
```

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Google::BillingSubaccount",
    "Properties" : {
        "<a href="#deletionpolicy" title="DeletionPolicy">DeletionPolicy</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#masterbillingaccount" title="MasterBillingAccount">MasterBillingAccount</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::Google::BillingSubaccount
Properties:
    <a href="#deletionpolicy" title="DeletionPolicy">DeletionPolicy</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#masterbillingaccount" title="MasterBillingAccount">MasterBillingAccount</a>: <i>String</i>
</pre>

## Properties

#### DeletionPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MasterBillingAccount

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

#### BillingAccountId

Returns the <code>BillingAccountId</code> value.

#### Id

Returns the <code>Id</code> value.

#### Name

Returns the <code>Name</code> value.

#### Open

Returns the <code>Open</code> value.

