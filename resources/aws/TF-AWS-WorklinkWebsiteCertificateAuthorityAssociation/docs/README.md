# TF::AWS::WorklinkWebsiteCertificateAuthorityAssociation

CloudFormation equivalent of aws_worklink_website_certificate_authority_association

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::AWS::WorklinkWebsiteCertificateAuthorityAssociation",
    "Properties" : {
        "<a href="#certificate" title="Certificate">Certificate</a>" : <i>String</i>,
        "<a href="#displayname" title="DisplayName">DisplayName</a>" : <i>String</i>,
        "<a href="#fleetarn" title="FleetArn">FleetArn</a>" : <i>String</i>,
    }
}
</pre>

### YAML

<pre>
Type: TF::AWS::WorklinkWebsiteCertificateAuthorityAssociation
Properties:
    <a href="#certificate" title="Certificate">Certificate</a>: <i>String</i>
    <a href="#displayname" title="DisplayName">DisplayName</a>: <i>String</i>
    <a href="#fleetarn" title="FleetArn">FleetArn</a>: <i>String</i>
</pre>

## Properties

#### Certificate

The root certificate of the Certificate Authority.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DisplayName

The certificate name to display.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### FleetArn

The ARN of the fleet.

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

#### WebsiteCaId

Returns the <code>WebsiteCaId</code> value.

