# Terraform::Google::BillingAccountIamPolicy

Allows management of the entire IAM policy for an existing Google Cloud Platform Billing Account.

~> **Warning:** Billing accounts have a default user that can be **overwritten**
by use of this resource. The safest alternative is to use multiple `google_billing_account_iam_binding`
   resources. If you do use this resource, the best way to be sure that you are
   not making dangerous changes is to start by importing your existing policy,
   and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_billing_account_iam_member` or `google_billing_account_iam_binding`
   or they will fight over what your policy should be.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::BillingAccountIamPolicy",
    "Properties" : {
        "<a href="#billingaccountid" title="BillingAccountId">BillingAccountId</a>" : <i>String</i>,
        "<a href="#policydata" title="PolicyData">PolicyData</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::BillingAccountIamPolicy
Properties:
    <a href="#billingaccountid" title="BillingAccountId">BillingAccountId</a>: <i>String</i>
    <a href="#policydata" title="PolicyData">PolicyData</a>: <i>String</i>
</pre>

## Properties

#### BillingAccountId

The billing account id.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyData

The `google_iam_policy` data source that represents
the IAM policy that will be applied to the billing account. This policy overrides any existing
policy applied to the billing account.

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

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.

