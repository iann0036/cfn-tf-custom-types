# TF::AD::GpoSecurity

CloudFormation equivalent of ad_gpo_security

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AD::GpoSecurity",
    "Properties" : {
        "<a href="#gpocontainer" title="GpoContainer">GpoContainer</a>" : <i>String</i>,
        "<a href="#accountlockout" title="AccountLockout">AccountLockout</a>" : <i>[ <a href="accountlockoutdefinition.md">AccountLockoutDefinition</a>, ... ]</i>,
        "<a href="#applicationlog" title="ApplicationLog">ApplicationLog</a>" : <i>[ <a href="applicationlogdefinition.md">ApplicationLogDefinition</a>, ... ]</i>,
        "<a href="#auditlog" title="AuditLog">AuditLog</a>" : <i>[ <a href="auditlogdefinition.md">AuditLogDefinition</a>, ... ]</i>,
        "<a href="#eventaudit" title="EventAudit">EventAudit</a>" : <i>[ <a href="eventauditdefinition.md">EventAuditDefinition</a>, ... ]</i>,
        "<a href="#filesystem" title="Filesystem">Filesystem</a>" : <i>[ <a href="filesystemdefinition.md">FilesystemDefinition</a>, ... ]</i>,
        "<a href="#kerberospolicy" title="KerberosPolicy">KerberosPolicy</a>" : <i>[ <a href="kerberospolicydefinition.md">KerberosPolicyDefinition</a>, ... ]</i>,
        "<a href="#passwordpolicies" title="PasswordPolicies">PasswordPolicies</a>" : <i>[ <a href="passwordpoliciesdefinition.md">PasswordPoliciesDefinition</a>, ... ]</i>,
        "<a href="#registrykeys" title="RegistryKeys">RegistryKeys</a>" : <i>[ <a href="registrykeysdefinition.md">RegistryKeysDefinition</a>, ... ]</i>,
        "<a href="#registryvalues" title="RegistryValues">RegistryValues</a>" : <i>[ <a href="registryvaluesdefinition.md">RegistryValuesDefinition</a>, ... ]</i>,
        "<a href="#restrictedgroups" title="RestrictedGroups">RestrictedGroups</a>" : <i>[ <a href="restrictedgroupsdefinition.md">RestrictedGroupsDefinition</a>, ... ]</i>,
        "<a href="#systemlog" title="SystemLog">SystemLog</a>" : <i>[ <a href="systemlogdefinition.md">SystemLogDefinition</a>, ... ]</i>,
        "<a href="#systemservices" title="SystemServices">SystemServices</a>" : <i>[ <a href="systemservicesdefinition.md">SystemServicesDefinition</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::AD::GpoSecurity
Properties:
    <a href="#gpocontainer" title="GpoContainer">GpoContainer</a>: <i>String</i>
    <a href="#accountlockout" title="AccountLockout">AccountLockout</a>: <i>
      - <a href="accountlockoutdefinition.md">AccountLockoutDefinition</a></i>
    <a href="#applicationlog" title="ApplicationLog">ApplicationLog</a>: <i>
      - <a href="applicationlogdefinition.md">ApplicationLogDefinition</a></i>
    <a href="#auditlog" title="AuditLog">AuditLog</a>: <i>
      - <a href="auditlogdefinition.md">AuditLogDefinition</a></i>
    <a href="#eventaudit" title="EventAudit">EventAudit</a>: <i>
      - <a href="eventauditdefinition.md">EventAuditDefinition</a></i>
    <a href="#filesystem" title="Filesystem">Filesystem</a>: <i>
      - <a href="filesystemdefinition.md">FilesystemDefinition</a></i>
    <a href="#kerberospolicy" title="KerberosPolicy">KerberosPolicy</a>: <i>
      - <a href="kerberospolicydefinition.md">KerberosPolicyDefinition</a></i>
    <a href="#passwordpolicies" title="PasswordPolicies">PasswordPolicies</a>: <i>
      - <a href="passwordpoliciesdefinition.md">PasswordPoliciesDefinition</a></i>
    <a href="#registrykeys" title="RegistryKeys">RegistryKeys</a>: <i>
      - <a href="registrykeysdefinition.md">RegistryKeysDefinition</a></i>
    <a href="#registryvalues" title="RegistryValues">RegistryValues</a>: <i>
      - <a href="registryvaluesdefinition.md">RegistryValuesDefinition</a></i>
    <a href="#restrictedgroups" title="RestrictedGroups">RestrictedGroups</a>: <i>
      - <a href="restrictedgroupsdefinition.md">RestrictedGroupsDefinition</a></i>
    <a href="#systemlog" title="SystemLog">SystemLog</a>: <i>
      - <a href="systemlogdefinition.md">SystemLogDefinition</a></i>
    <a href="#systemservices" title="SystemServices">SystemServices</a>: <i>
      - <a href="systemservicesdefinition.md">SystemServicesDefinition</a></i>
</pre>

## Properties

#### GpoContainer

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AccountLockout

_Required_: No

_Type_: List of <a href="accountlockoutdefinition.md">AccountLockoutDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ApplicationLog

_Required_: No

_Type_: List of <a href="applicationlogdefinition.md">ApplicationLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuditLog

_Required_: No

_Type_: List of <a href="auditlogdefinition.md">AuditLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EventAudit

_Required_: No

_Type_: List of <a href="eventauditdefinition.md">EventAuditDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Filesystem

_Required_: No

_Type_: List of <a href="filesystemdefinition.md">FilesystemDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### KerberosPolicy

_Required_: No

_Type_: List of <a href="kerberospolicydefinition.md">KerberosPolicyDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PasswordPolicies

_Required_: No

_Type_: List of <a href="passwordpoliciesdefinition.md">PasswordPoliciesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryKeys

_Required_: No

_Type_: List of <a href="registrykeysdefinition.md">RegistryKeysDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RegistryValues

_Required_: No

_Type_: List of <a href="registryvaluesdefinition.md">RegistryValuesDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RestrictedGroups

_Required_: No

_Type_: List of <a href="restrictedgroupsdefinition.md">RestrictedGroupsDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemLog

_Required_: No

_Type_: List of <a href="systemlogdefinition.md">SystemLogDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SystemServices

_Required_: No

_Type_: List of <a href="systemservicesdefinition.md">SystemServicesDefinition</a>

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

