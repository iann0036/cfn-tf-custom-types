# Terraform::AzureAD::ServicePrincipal

Manages a Service Principal associated with an Application within Azure Active Directory.

-> **NOTE:** If you're authenticating using a Service Principal then it must have permissions to both `Read and write all applications` and `Sign in and read user profile` within the `Windows Azure Active Directory` API. Please see The [Granting a Service Principal permission to manage AAD](../guides/service_principal_configuration.html) for the required steps.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AzureAD::ServicePrincipal",
    "Properties" : {
        "<a href="#approleassignmentrequired" title="AppRoleAssignmentRequired">AppRoleAssignmentRequired</a>" : <i>Boolean</i>,
        "<a href="#applicationid" title="ApplicationId">ApplicationId</a>" : <i>String</i>,
        "<a href="#tags" title="Tags">Tags</a>" : <i>[ String, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AzureAD::ServicePrincipal
Properties:
    <a href="#approleassignmentrequired" title="AppRoleAssignmentRequired">AppRoleAssignmentRequired</a>: <i>Boolean</i>
    <a href="#applicationid" title="ApplicationId">ApplicationId</a>: <i>String</i>
    <a href="#tags" title="Tags">Tags</a>: <i>
      - String</i>
</pre>

## Properties

#### AppRoleAssignmentRequired

Does this Service Principal require an AppRoleAssignment to a user or group before Azure AD will issue a user or access token to the application? Defaults to `false`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationId

The ID of the Azure AD Application for which to create a Service Principal.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Tags

A list of tags to apply to the Service Principal.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### DisplayName

Returns the <code>DisplayName</code> value.

#### ObjectId

Returns the <code>ObjectId</code> value.

