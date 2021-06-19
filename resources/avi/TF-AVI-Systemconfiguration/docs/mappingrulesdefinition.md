# TF::AVI::Systemconfiguration MappingRulesDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#assignpolicy" title="AssignPolicy">AssignPolicy</a>" : <i>String</i>,
    "<a href="#assignrole" title="AssignRole">AssignRole</a>" : <i>String</i>,
    "<a href="#assigntenant" title="AssignTenant">AssignTenant</a>" : <i>String</i>,
    "<a href="#assignuserprofile" title="AssignUserprofile">AssignUserprofile</a>" : <i>String</i>,
    "<a href="#index" title="Index">Index</a>" : <i>Double</i>,
    "<a href="#issuperuser" title="IsSuperuser">IsSuperuser</a>" : <i>Boolean</i>,
    "<a href="#policyattributename" title="PolicyAttributeName">PolicyAttributeName</a>" : <i>String</i>,
    "<a href="#roleattributename" title="RoleAttributeName">RoleAttributeName</a>" : <i>String</i>,
    "<a href="#rolerefs" title="RoleRefs">RoleRefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#tenantattributename" title="TenantAttributeName">TenantAttributeName</a>" : <i>String</i>,
    "<a href="#tenantrefs" title="TenantRefs">TenantRefs</a>" : <i>[ String, ... ]</i>,
    "<a href="#userprofileattributename" title="UserprofileAttributeName">UserprofileAttributeName</a>" : <i>String</i>,
    "<a href="#userprofileref" title="UserprofileRef">UserprofileRef</a>" : <i>String</i>,
    "<a href="#attributematch" title="AttributeMatch">AttributeMatch</a>" : <i>[ <a href="attributematchdefinition.md">AttributeMatchDefinition</a>, ... ]</i>,
    "<a href="#groupmatch" title="GroupMatch">GroupMatch</a>" : <i>[ <a href="groupmatchdefinition.md">GroupMatchDefinition</a>, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#assignpolicy" title="AssignPolicy">AssignPolicy</a>: <i>String</i>
<a href="#assignrole" title="AssignRole">AssignRole</a>: <i>String</i>
<a href="#assigntenant" title="AssignTenant">AssignTenant</a>: <i>String</i>
<a href="#assignuserprofile" title="AssignUserprofile">AssignUserprofile</a>: <i>String</i>
<a href="#index" title="Index">Index</a>: <i>Double</i>
<a href="#issuperuser" title="IsSuperuser">IsSuperuser</a>: <i>Boolean</i>
<a href="#policyattributename" title="PolicyAttributeName">PolicyAttributeName</a>: <i>String</i>
<a href="#roleattributename" title="RoleAttributeName">RoleAttributeName</a>: <i>String</i>
<a href="#rolerefs" title="RoleRefs">RoleRefs</a>: <i>
      - String</i>
<a href="#tenantattributename" title="TenantAttributeName">TenantAttributeName</a>: <i>String</i>
<a href="#tenantrefs" title="TenantRefs">TenantRefs</a>: <i>
      - String</i>
<a href="#userprofileattributename" title="UserprofileAttributeName">UserprofileAttributeName</a>: <i>String</i>
<a href="#userprofileref" title="UserprofileRef">UserprofileRef</a>: <i>String</i>
<a href="#attributematch" title="AttributeMatch">AttributeMatch</a>: <i>
      - <a href="attributematchdefinition.md">AttributeMatchDefinition</a></i>
<a href="#groupmatch" title="GroupMatch">GroupMatch</a>: <i>
      - <a href="groupmatchdefinition.md">GroupMatchDefinition</a></i>
</pre>

## Properties

#### AssignPolicy

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignRole

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignTenant

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AssignUserprofile

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Index

_Required_: Yes

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### IsSuperuser

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PolicyAttributeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleAttributeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleRefs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantAttributeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TenantRefs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserprofileAttributeName

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### UserprofileRef

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AttributeMatch

_Required_: No

_Type_: List of <a href="attributematchdefinition.md">AttributeMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### GroupMatch

_Required_: No

_Type_: List of <a href="groupmatchdefinition.md">GroupMatchDefinition</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

