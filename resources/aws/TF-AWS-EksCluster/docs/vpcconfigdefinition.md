# TF::AWS::EksCluster VpcConfigDefinition

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#endpointprivateaccess" title="EndpointPrivateAccess">EndpointPrivateAccess</a>" : <i>Boolean</i>,
    "<a href="#endpointpublicaccess" title="EndpointPublicAccess">EndpointPublicAccess</a>" : <i>Boolean</i>,
    "<a href="#publicaccesscidrs" title="PublicAccessCidrs">PublicAccessCidrs</a>" : <i>[ String, ... ]</i>,
    "<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>" : <i>[ String, ... ]</i>,
    "<a href="#subnetids" title="SubnetIds">SubnetIds</a>" : <i>[ String, ... ]</i>
}
</pre>

### YAML

<pre>
<a href="#endpointprivateaccess" title="EndpointPrivateAccess">EndpointPrivateAccess</a>: <i>Boolean</i>
<a href="#endpointpublicaccess" title="EndpointPublicAccess">EndpointPublicAccess</a>: <i>Boolean</i>
<a href="#publicaccesscidrs" title="PublicAccessCidrs">PublicAccessCidrs</a>: <i>
      - String</i>
<a href="#securitygroupids" title="SecurityGroupIds">SecurityGroupIds</a>: <i>
      - String</i>
<a href="#subnetids" title="SubnetIds">SubnetIds</a>: <i>
      - String</i>
</pre>

## Properties

#### EndpointPrivateAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### EndpointPublicAccess

_Required_: No

_Type_: Boolean

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### PublicAccessCidrs

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityGroupIds

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SubnetIds

_Required_: Yes

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

