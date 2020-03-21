# Terraform::Google::OrganizationIamPolicy

Allows management of the entire IAM policy for an existing Google Cloud Platform Organization.

!> **Warning:** New organizations have several default policies which will,
   without extreme caution, be **overwritten** by use of this resource.
   The safest alternative is to use multiple `google_organization_iam_binding`
   resources.  It is easy to use this resource to remove your own access to
   an organization, which will require a call to Google Support to have
   fixed, and can take multiple days to resolve.  If you do use this resource,
   the best way to be sure that you are not making dangerous changes is to start
   by importing your existing policy, and examining the diff very closely.

~> **Note:** This resource __must not__ be used in conjunction with
   `google_organization_iam_member` or `google_organization_iam_binding`
   or they will fight over what your policy should be.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::OrganizationIamPolicy",
    "Properties" : {
        "<a href="#orgid" title="OrgId">OrgId</a>" : <i>String</i>,
        "<a href="#policydata" title="PolicyData">PolicyData</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::OrganizationIamPolicy
Properties:
    <a href="#orgid" title="OrgId">OrgId</a>: <i>String</i>
    <a href="#policydata" title="PolicyData">PolicyData</a>: <i>String</i>
</pre>

## Properties

#### OrgId

The numeric ID of the organization in which you want to create a custom role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyData

The `google_iam_policy` data source that represents
the IAM policy that will be applied to the organization. This policy overrides any existing
policy applied to the organization.

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

#### Etag

Returns the <code>Etag</code> value.

