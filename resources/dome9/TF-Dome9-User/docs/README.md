# TF::Dome9::User

The User resource has methods to create and manage Dome9 users.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Dome9::User",
    "Properties" : {
        "<a href="#create" title="Create">Create</a>" : <i>[ String, ... ]</i>,
        "<a href="#crossaccountaccess" title="CrossAccountAccess">CrossAccountAccess</a>" : <i>[ String, ... ]</i>,
        "<a href="#email" title="Email">Email</a>" : <i>String</i>,
        "<a href="#firstname" title="FirstName">FirstName</a>" : <i>String</i>,
        "<a href="#isowner" title="IsOwner">IsOwner</a>" : <i>Boolean</i>,
        "<a href="#isssoenabled" title="IsSsoEnabled">IsSsoEnabled</a>" : <i>Boolean</i>,
        "<a href="#lastname" title="LastName">LastName</a>" : <i>String</i>,
        "<a href="#permitalertactions" title="PermitAlertActions">PermitAlertActions</a>" : <i>Boolean</i>,
        "<a href="#permitnotifications" title="PermitNotifications">PermitNotifications</a>" : <i>Boolean</i>,
        "<a href="#permitonboarding" title="PermitOnBoarding">PermitOnBoarding</a>" : <i>Boolean</i>,
        "<a href="#permitpolicies" title="PermitPolicies">PermitPolicies</a>" : <i>Boolean</i>,
        "<a href="#permitrulesets" title="PermitRulesets">PermitRulesets</a>" : <i>Boolean</i>,
        "<a href="#roleids" title="RoleIds">RoleIds</a>" : <i>[ Double, ... ]</i>,
        "<a href="#access" title="Access">Access</a>" : <i>[ <a href="accessdefinition.md">AccessDefinition</a>, ... ]</i>,
        "<a href="#manage" title="Manage">Manage</a>" : <i>[ <a href="managedefinition.md">ManageDefinition</a>, ... ]</i>,
        "<a href="#view" title="View">View</a>" : <i>[ <a href="viewdefinition.md">ViewDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Dome9::User
Properties:
    <a href="#create" title="Create">Create</a>: <i>
      - String</i>
    <a href="#crossaccountaccess" title="CrossAccountAccess">CrossAccountAccess</a>: <i>
      - String</i>
    <a href="#email" title="Email">Email</a>: <i>String</i>
    <a href="#firstname" title="FirstName">FirstName</a>: <i>String</i>
    <a href="#isowner" title="IsOwner">IsOwner</a>: <i>Boolean</i>
    <a href="#isssoenabled" title="IsSsoEnabled">IsSsoEnabled</a>: <i>Boolean</i>
    <a href="#lastname" title="LastName">LastName</a>: <i>String</i>
    <a href="#permitalertactions" title="PermitAlertActions">PermitAlertActions</a>: <i>Boolean</i>
    <a href="#permitnotifications" title="PermitNotifications">PermitNotifications</a>: <i>Boolean</i>
    <a href="#permitonboarding" title="PermitOnBoarding">PermitOnBoarding</a>: <i>Boolean</i>
    <a href="#permitpolicies" title="PermitPolicies">PermitPolicies</a>: <i>Boolean</i>
    <a href="#permitrulesets" title="PermitRulesets">PermitRulesets</a>: <i>Boolean</i>
    <a href="#roleids" title="RoleIds">RoleIds</a>: <i>
      - Double</i>
    <a href="#access" title="Access">Access</a>: <i>
      - <a href="accessdefinition.md">AccessDefinition</a></i>
    <a href="#manage" title="Manage">Manage</a>: <i>
      - <a href="managedefinition.md">ManageDefinition</a></i>
    <a href="#view" title="View">View</a>: <i>
      - <a href="viewdefinition.md">ViewDefinition</a></i>
</pre>

## Properties

#### Create

Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### CrossAccountAccess

Cross account access.
* `create` - (Optional) Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Email

user email.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FirstName

userfirst name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsOwner

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSsoEnabled

user has enabled SSO sign-on.

_Required_: Yes

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### LastName

user last name.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitAlertActions

Is permitted permit alert actions (Optional) .
* `permit_on_boarding` - Is permitted permit on boarding (Optional)  .
* `cross_account_access` - (Optional) Cross account access.
* `create` - (Optional) Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitNotifications

Is permitted permit notifications (Optional) .
* `permit_policies` - Is permitted permit policies (Optional) .
* `permit_alert_actions` - Is permitted permit alert actions (Optional) .
* `permit_on_boarding` - Is permitted permit on boarding (Optional)  .
* `cross_account_access` - (Optional) Cross account access.
* `create` - (Optional) Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitOnBoarding

Is permitted permit on boarding (Optional)  .
* `cross_account_access` - (Optional) Cross account access.
* `create` - (Optional) Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitPolicies

Is permitted permit policies (Optional) .
* `permit_alert_actions` - Is permitted permit alert actions (Optional) .
* `permit_on_boarding` - Is permitted permit on boarding (Optional)  .
* `cross_account_access` - (Optional) Cross account access.
* `create` - (Optional) Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PermitRulesets

Is permitted permit rulesets (Optional) .
* `permit_notifications` - Is permitted permit notifications (Optional) .
* `permit_policies` - Is permitted permit policies (Optional) .
* `permit_alert_actions` - Is permitted permit alert actions (Optional) .
* `permit_on_boarding` - Is permitted permit on boarding (Optional)  .
* `cross_account_access` - (Optional) Cross account access.
* `create` - (Optional) Create permission list.
* `access` - (Optional) Access permission list ([SRL](#SRL) Type).
* `view` - (Optional) View permission list ([SRL](#SRL) Type).
* `manage` - (Optional) Manage permission list ([SRL](#SRL) Type).

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleIds

_Required_: No

_Type_: List of Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Access

_Required_: No

_Type_: List of <a href="accessdefinition.md">AccessDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Manage

_Required_: No

_Type_: List of <a href="managedefinition.md">ManageDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### View

_Required_: No

_Type_: List of <a href="viewdefinition.md">ViewDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### CanSwitchRole

Returns the <code>CanSwitchRole</code> value.

#### HasApiKey

Returns the <code>HasApiKey</code> value.

#### HasApiKeyV1

Returns the <code>HasApiKeyV1</code> value.

#### HasApiKeyV2

Returns the <code>HasApiKeyV2</code> value.

#### IamSafe

Returns the <code>IamSafe</code> value.

#### Id

Returns the <code>Id</code> value.

#### IsAuditor

Returns the <code>IsAuditor</code> value.

#### IsLocked

Returns the <code>IsLocked</code> value.

#### IsMfaEnabled

Returns the <code>IsMfaEnabled</code> value.

#### IsMobileDevicePaired

Returns the <code>IsMobileDevicePaired</code> value.

#### IsSuperUser

Returns the <code>IsSuperUser</code> value.

#### IsSuspended

Returns the <code>IsSuspended</code> value.

#### LastLogin

Returns the <code>LastLogin</code> value.

