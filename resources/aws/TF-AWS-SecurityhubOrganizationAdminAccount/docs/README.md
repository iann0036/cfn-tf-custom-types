# TF::AWS::SecurityhubOrganizationAdminAccount

Manages a Security Hub administrator account for an organization. The AWS account utilizing this resource must be an Organizations primary account. More information about Organizations support in Security Hub can be found in the [Security Hub User Guide](https://docs.aws.amazon.com/securityhub/latest/userguide/designate-orgs-admin-account.html).

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::SecurityhubOrganizationAdminAccount",
    "Properties" : {
        "<a href="#adminaccountid" title="AdminAccountId">AdminAccountId</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::SecurityhubOrganizationAdminAccount
Properties:
    <a href="#adminaccountid" title="AdminAccountId">AdminAccountId</a>: <i>String</i>
</pre>

## Properties

#### AdminAccountId

The AWS account identifier of the account to designate as the Security Hub administrator account.

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

