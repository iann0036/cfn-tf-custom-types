# TF::Aviatrix::SegmentationSecurityDomainAssociation

The **aviatrix_segmentation_security_domain_association** resource handles creation of [Transit Segmentation](https://docs.aviatrix.com/HowTos/transit_segmentation_faq.html) Security Domain and Transit Gateway Attachment Associations.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "TF::Aviatrix::SegmentationSecurityDomainAssociation",
    "Properties" : {
        "<a href="#attachmentname" title="AttachmentName">AttachmentName</a>" : <i>String</i>,
        "<a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>" : <i>String</i>,
        "<a href="#transitgatewayname" title="TransitGatewayName">TransitGatewayName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: TF::Aviatrix::SegmentationSecurityDomainAssociation
Properties:
    <a href="#attachmentname" title="AttachmentName">AttachmentName</a>: <i>String</i>
    <a href="#securitydomainname" title="SecurityDomainName">SecurityDomainName</a>: <i>String</i>
    <a href="#transitgatewayname" title="TransitGatewayName">TransitGatewayName</a>: <i>String</i>
</pre>

## Properties

#### AttachmentName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecurityDomainName

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### TransitGatewayName

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
