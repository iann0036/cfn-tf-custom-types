# Terraform::Vault::AwsAuthBackendRole

CloudFormation equivalent of vault_aws_auth_backend_role

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::AwsAuthBackendRole",
    "Properties" : {
        "<a href="#allowinstancemigration" title="AllowInstanceMigration">AllowInstanceMigration</a>" : <i>Boolean</i>,
        "<a href="#authtype" title="AuthType">AuthType</a>" : <i>String</i>,
        "<a href="#backend" title="Backend">Backend</a>" : <i>String</i>,
        "<a href="#boundaccountid" title="BoundAccountId">BoundAccountId</a>" : <i>String</i>,
        "<a href="#boundaccountids" title="BoundAccountIds">BoundAccountIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundamiid" title="BoundAmiId">BoundAmiId</a>" : <i>String</i>,
        "<a href="#boundamiids" title="BoundAmiIds">BoundAmiIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundec2instanceid" title="BoundEc2InstanceId">BoundEc2InstanceId</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundec2instanceids" title="BoundEc2InstanceIds">BoundEc2InstanceIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundiaminstanceprofilearn" title="BoundIamInstanceProfileArn">BoundIamInstanceProfileArn</a>" : <i>String</i>,
        "<a href="#boundiaminstanceprofilearns" title="BoundIamInstanceProfileArns">BoundIamInstanceProfileArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundiamprincipalarn" title="BoundIamPrincipalArn">BoundIamPrincipalArn</a>" : <i>String</i>,
        "<a href="#boundiamprincipalarns" title="BoundIamPrincipalArns">BoundIamPrincipalArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundiamrolearn" title="BoundIamRoleArn">BoundIamRoleArn</a>" : <i>String</i>,
        "<a href="#boundiamrolearns" title="BoundIamRoleArns">BoundIamRoleArns</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundregion" title="BoundRegion">BoundRegion</a>" : <i>String</i>,
        "<a href="#boundregions" title="BoundRegions">BoundRegions</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundsubnetid" title="BoundSubnetId">BoundSubnetId</a>" : <i>String</i>,
        "<a href="#boundsubnetids" title="BoundSubnetIds">BoundSubnetIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#boundvpcid" title="BoundVpcId">BoundVpcId</a>" : <i>String</i>,
        "<a href="#boundvpcids" title="BoundVpcIds">BoundVpcIds</a>" : <i>[ String, ... ]</i>,
        "<a href="#disallowreauthentication" title="DisallowReauthentication">DisallowReauthentication</a>" : <i>Boolean</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#inferredawsregion" title="InferredAwsRegion">InferredAwsRegion</a>" : <i>String</i>,
        "<a href="#inferredentitytype" title="InferredEntityType">InferredEntityType</a>" : <i>String</i>,
        "<a href="#maxttl" title="MaxTtl">MaxTtl</a>" : <i>Double</i>,
        "<a href="#period" title="Period">Period</a>" : <i>Double</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#resolveawsuniqueids" title="ResolveAwsUniqueIds">ResolveAwsUniqueIds</a>" : <i>Boolean</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#roletag" title="RoleTag">RoleTag</a>" : <i>String</i>,
        "<a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>" : <i>Double</i>,
        "<a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>" : <i>Boolean</i>,
        "<a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>" : <i>Double</i>,
        "<a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>" : <i>Double</i>,
        "<a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>" : <i>[ String, ... ]</i>,
        "<a href="#tokenttl" title="TokenTtl">TokenTtl</a>" : <i>Double</i>,
        "<a href="#tokentype" title="TokenType">TokenType</a>" : <i>String</i>,
        "<a href="#ttl" title="Ttl">Ttl</a>" : <i>Double</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::AwsAuthBackendRole
Properties:
    <a href="#allowinstancemigration" title="AllowInstanceMigration">AllowInstanceMigration</a>: <i>Boolean</i>
    <a href="#authtype" title="AuthType">AuthType</a>: <i>String</i>
    <a href="#backend" title="Backend">Backend</a>: <i>String</i>
    <a href="#boundaccountid" title="BoundAccountId">BoundAccountId</a>: <i>String</i>
    <a href="#boundaccountids" title="BoundAccountIds">BoundAccountIds</a>: <i>
      - String</i>
    <a href="#boundamiid" title="BoundAmiId">BoundAmiId</a>: <i>String</i>
    <a href="#boundamiids" title="BoundAmiIds">BoundAmiIds</a>: <i>
      - String</i>
    <a href="#boundec2instanceid" title="BoundEc2InstanceId">BoundEc2InstanceId</a>: <i>
      - String</i>
    <a href="#boundec2instanceids" title="BoundEc2InstanceIds">BoundEc2InstanceIds</a>: <i>
      - String</i>
    <a href="#boundiaminstanceprofilearn" title="BoundIamInstanceProfileArn">BoundIamInstanceProfileArn</a>: <i>String</i>
    <a href="#boundiaminstanceprofilearns" title="BoundIamInstanceProfileArns">BoundIamInstanceProfileArns</a>: <i>
      - String</i>
    <a href="#boundiamprincipalarn" title="BoundIamPrincipalArn">BoundIamPrincipalArn</a>: <i>String</i>
    <a href="#boundiamprincipalarns" title="BoundIamPrincipalArns">BoundIamPrincipalArns</a>: <i>
      - String</i>
    <a href="#boundiamrolearn" title="BoundIamRoleArn">BoundIamRoleArn</a>: <i>String</i>
    <a href="#boundiamrolearns" title="BoundIamRoleArns">BoundIamRoleArns</a>: <i>
      - String</i>
    <a href="#boundregion" title="BoundRegion">BoundRegion</a>: <i>String</i>
    <a href="#boundregions" title="BoundRegions">BoundRegions</a>: <i>
      - String</i>
    <a href="#boundsubnetid" title="BoundSubnetId">BoundSubnetId</a>: <i>String</i>
    <a href="#boundsubnetids" title="BoundSubnetIds">BoundSubnetIds</a>: <i>
      - String</i>
    <a href="#boundvpcid" title="BoundVpcId">BoundVpcId</a>: <i>String</i>
    <a href="#boundvpcids" title="BoundVpcIds">BoundVpcIds</a>: <i>
      - String</i>
    <a href="#disallowreauthentication" title="DisallowReauthentication">DisallowReauthentication</a>: <i>Boolean</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#inferredawsregion" title="InferredAwsRegion">InferredAwsRegion</a>: <i>String</i>
    <a href="#inferredentitytype" title="InferredEntityType">InferredEntityType</a>: <i>String</i>
    <a href="#maxttl" title="MaxTtl">MaxTtl</a>: <i>Double</i>
    <a href="#period" title="Period">Period</a>: <i>Double</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#resolveawsuniqueids" title="ResolveAwsUniqueIds">ResolveAwsUniqueIds</a>: <i>Boolean</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#roletag" title="RoleTag">RoleTag</a>: <i>String</i>
    <a href="#tokenboundcidrs" title="TokenBoundCidrs">TokenBoundCidrs</a>: <i>
      - String</i>
    <a href="#tokenexplicitmaxttl" title="TokenExplicitMaxTtl">TokenExplicitMaxTtl</a>: <i>Double</i>
    <a href="#tokenmaxttl" title="TokenMaxTtl">TokenMaxTtl</a>: <i>Double</i>
    <a href="#tokennodefaultpolicy" title="TokenNoDefaultPolicy">TokenNoDefaultPolicy</a>: <i>Boolean</i>
    <a href="#tokennumuses" title="TokenNumUses">TokenNumUses</a>: <i>Double</i>
    <a href="#tokenperiod" title="TokenPeriod">TokenPeriod</a>: <i>Double</i>
    <a href="#tokenpolicies" title="TokenPolicies">TokenPolicies</a>: <i>
      - String</i>
    <a href="#tokenttl" title="TokenTtl">TokenTtl</a>: <i>Double</i>
    <a href="#tokentype" title="TokenType">TokenType</a>: <i>String</i>
    <a href="#ttl" title="Ttl">Ttl</a>: <i>Double</i>
</pre>

## Properties

#### AllowInstanceMigration

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Backend

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAccountId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAccountIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAmiId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAmiIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundEc2InstanceId

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundEc2InstanceIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamInstanceProfileArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamInstanceProfileArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamPrincipalArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamPrincipalArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamRoleArns

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundRegions

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundSubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundSubnetIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundVpcIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisallowReauthentication

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InferredAwsRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InferredEntityType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### MaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Period

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### ResolveAwsUniqueIds

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleTag

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenBoundCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenExplicitMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenMaxTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNoDefaultPolicy

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenNumUses

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPeriod

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenPolicies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenTtl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TokenType

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Ttl

_Required_: No

_Type_: Double

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

