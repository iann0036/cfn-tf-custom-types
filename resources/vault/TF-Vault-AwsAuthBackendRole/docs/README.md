# TF::Vault::AwsAuthBackendRole

Manages an AWS auth backend role in a Vault server. Roles constrain the
instances or principals that can perform the login operation against the
backend. See the [Vault
documentation](https://www.vaultproject.io/docs/auth/aws.html) for more
information.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Vault::AwsAuthBackendRole",
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
Type: TF::Vault::AwsAuthBackendRole
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

If set to `true`, allows migration of
the underlying instance where the client resides.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### AuthType

The auth type permitted for this role. Valid choices
are `ec2` and `iam`. Defaults to `iam`.

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

If set, defines a constraint on the EC2
instances that can perform the login operation that they should be using the
account ID specified by this field. `auth_type` must be set to `ec2` or
`inferred_entity_type` must be set to `ec2_instance` to use this constraint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAmiId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundAmiIds

If set, defines a constraint on the EC2 instances
that can perform the login operation that they should be using the AMI ID
specified by this field. `auth_type` must be set to `ec2` or
`inferred_entity_type` must be set to `ec2_instance` to use this constraint.

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

If set, defines a constraint on
the EC2 instances that can perform the login operation that they must be
associated with an IAM instance profile ARN which has a prefix that matches
the value specified by this field. The value is prefix-matched as though it
were a glob ending in `*`. `auth_type` must be set to `ec2` or
`inferred_entity_type` must be set to `ec2_instance` to use this constraint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamPrincipalArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamPrincipalArns

If set, defines the IAM principal that
must be authenticated when `auth_type` is set to `iam`. Wildcards are
supported at the end of the ARN.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamRoleArn

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundIamRoleArns

If set, defines a constraint on the EC2
instances that can perform the login operation that they must match the IAM
role ARN specified by this field. `auth_type` must be set to `ec2` or
`inferred_entity_type` must be set to `ec2_instance` to use this constraint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundRegion

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundRegions

If set, defines a constraint on the EC2 instances
that can perform the login operation that the region in their identity
document must match the one specified by this field. `auth_type` must be set
to `ec2` or `inferred_entity_type` must be set to `ec2_instance` to use this
constraint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundSubnetId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundSubnetIds

If set, defines a constraint on the EC2
instances that can perform the login operation that they be associated with
the subnet ID that matches the value specified by this field. `auth_type`
must be set to `ec2` or `inferred_entity_type` must be set to `ec2_instance`
to use this constraint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundVpcId

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### BoundVpcIds

If set, defines a constraint on the EC2 instances
that can perform the login operation that they be associated with the VPC ID
that matches the value specified by this field. `auth_type` must be set to
`ec2` or `inferred_entity_type` must be set to `ec2_instance` to use this
constraint.

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisallowReauthentication

IF set to `true`, only allows a
single token to be granted per instance ID. This can only be set when
`auth_type` is set to `ec2`.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InferredAwsRegion

When `inferred_entity_type` is set, this
is the region to search for the inferred entities. Required if
`inferred_entity_type` is set. This only applies when `auth_type` is set to
`iam`.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### InferredEntityType

If set, instructs Vault to turn on
inferencing. The only valid value is `ec2_instance`, which instructs Vault to
infer that the role comes from an EC2 instance in an IAM instance profile.
This only applies when `auth_type` is set to `iam`.

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

Only valid when
`auth_type` is `iam`. If set to `true`, the `bound_iam_principal_arns` are
resolved to [AWS Unique
IDs](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids)
for the bound principal ARN. This field is ignored when a
`bound_iam_principal_arn` ends in a wildcard. Resolving to unique IDs more
closely mimics the behavior of AWS services in that if an IAM user or role is
deleted and a new one is recreated with the same name, those new users or
roles won't get access to roles in Vault that were permissioned to the prior
principals of the same name. Defaults to `true`.
Once set to `true`, this cannot be changed to `false` without recreating the role.

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

The name of the role.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### RoleTag

If set, enable role tags for this role. The value set
for this field should be the key of the tag on the EC2 instance. `auth_type`
must be set to `ec2` or `inferred_entity_type` must be set to `ec2_instance`
to use this constraint.

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

#### Id

Returns the <code>Id</code> value.

